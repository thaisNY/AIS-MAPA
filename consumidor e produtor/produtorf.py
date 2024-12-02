import pika
import json

# Configurações do Amazon MQ
MQ_HOST = 'b-43a58687-c7df-40e3-9f81-398b4a8572cf-1.mq.us-east-1.amazonaws.com'
MQ_PORT = 5671
MQ_USERNAME = 'meu_usuario'
MQ_PASSWORD = 'minha_senha1'

class Consumer:
    def __init__(self, queue_name='restaurant_data'):
        self.queue_name = queue_name
        self.connection = None
        self.channel = None

    def connect(self):
        """Estabelece conexão com o Amazon MQ."""
        credentials = pika.PlainCredentials(MQ_USERNAME, MQ_PASSWORD)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=MQ_HOST,
                port=MQ_PORT,
                credentials=credentials,
                ssl_options=pika.SSLOptions()
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        print(f"Conectado ao Amazon MQ e aguardando mensagens na fila '{self.queue_name}'")

    def start_consuming(self, callback):
        """Inicia o consumo de mensagens."""
        if not self.channel:
            raise Exception("Conexão não estabelecida. Chame 'connect' antes de consumir mensagens.")

        def on_message(ch, method, properties, body):
            message = json.loads(body)
            callback(message)  # Passa a mensagem para o callback externo

        self.channel.basic_consume(queue=self.queue_name, on_message_callback=on_message, auto_ack=True)
        print("Iniciando o consumo de mensagens...")
        self.channel.start_consuming()

    def close(self):
        """Fecha a conexão com o Amazon MQ."""
        if self.connection:
            self.connection.close()
            print("Conexão encerrada com o Amazon MQ.")
