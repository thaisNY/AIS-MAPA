import pika
import boto3
import pandas as pd
from geopy.distance import geodesic
import folium
import json

# Configurações do AWS MQ e S3
MQ_HOST = 'seu-broker.mq.us-east-1.amazonaws.com'  # Substitua com o endereço do MQ
MQ_USERNAME = 'seu_usuario'
MQ_PASSWORD = 'sua_senha'
BUCKET_NAME = 'ais-proj-final'  # Nome do seu bucket S3
FILE_KEY = 'zomato.csv'         # Nome do arquivo no bucket

# Função para gerar o mapa
def generate_map(latitude, longitude, restaurants):
    m = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup="Você está aqui!", icon=folium.Icon(color="blue")).add_to(m)

    for _, row in restaurants.iterrows():
        folium.Marker(
            [row['Latitude'], row['Longitude']],
            popup=f"{row['Restaurant Name']} - {row['distance']:.2f} km",
            icon=folium.Icon(color="red")
        ).add_to(m)

    m.save("templates/map.html")
    print("Mapa gerado em templates/map.html")

# Função callback para processar mensagens do MQ
def callback(ch, method, properties, body):
    message = json.loads(body)
    latitude = message['latitude']
    longitude = message['longitude']
    max_distance = message['max_distance']

    # Baixar o arquivo do S3
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, FILE_KEY, 'local_restaurants.csv')
    df = pd.read_csv('local_restaurants.csv')

    # Filtrar restaurantes próximos
    user_location = (latitude, longitude)
    df['distance'] = df.apply(
        lambda row: geodesic(user_location, (row['Latitude'], row['Longitude'])).km, axis=1
    )
    nearby_restaurants = df[df['distance'] <= max_distance].sort_values(by='distance')

    # Gerar o mapa
    generate_map(latitude, longitude, nearby_restaurants)

# Configuração do consumidor do AWS MQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=MQ_HOST,
        credentials=pika.PlainCredentials(MQ_USERNAME, MQ_PASSWORD),
        ssl=True
    )
)
channel = connection.channel()
channel.queue_declare(queue='search_requests')

channel.basic_consume(queue='search_requests', on_message_callback=callback, auto_ack=True)
print('Aguardando mensagens...')
channel.start_consuming()
