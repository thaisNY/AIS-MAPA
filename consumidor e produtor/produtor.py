import pika
import json

MQ_HOST = 'seu-broker.mq.us-east-1.amazonaws.com'  # Substitua pelo endereço do MQ
MQ_USERNAME = 'seu_usuario'
MQ_PASSWORD = 'sua_senha'

def send_message(latitude, longitude, max_distance):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=MQ_HOST,
            credentials=pika.PlainCredentials(MQ_USERNAME, MQ_PASSWORD),
            ssl=True
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue='search_requests')

    message = {
        'latitude': latitude,
        'longitude': longitude,
        'max_distance': max_distance
    }
    channel.basic_publish(exchange='', routing_key='search_requests', body=json.dumps(message))
    print("Mensagem enviada:", message)
    connection.close()

# Teste enviando uma mensagem
send_message(-23.563210, -46.654250, 5)
