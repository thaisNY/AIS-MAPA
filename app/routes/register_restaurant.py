from flask import Blueprint, jsonify, current_app
from json import loads
import stomp as st
from ..models.restaurant import Restaurant

# Criando o Blueprint
register_restaurant_bp = Blueprint('register', __name__)

@register_restaurant_bp.route('/', methods=['GET'])
def register_new_geolocation():
    return jsonify({'message': 'List of users'})

@register_restaurant_bp.route('/collection', methods=['GET'])
def register_collection():
    class Listener(st.ConnectionListener):
        def __init__(self, app):
            self.app = app  # Passar a instância do app Flask

        def on_message(self, frame):
            print("Mensagem recebida!")
            # Garantir contexto da aplicação
            with self.app.app_context():
                try:
                    rest = Restaurant()
                    data = loads(frame.body)  # Converter JSON string para dicionário
                    rest.register_restaurants(data)
                except Exception as e:
                    print(f"Erro ao processar mensagem: {e}")

    # Criar listener com contexto do Flask
    listener = Listener(current_app._get_current_object()) # type: ignore
    queue_address = ('localhost', 61613)
    queue_conn = st.Connection([queue_address])
    queue_conn.set_listener("", listener)
    queue_conn.connect(wait=True)
    queue_conn.subscribe(destination='/queue/server_queue', id=1)

    return jsonify({'message': 'Processamento concluido'}), 200
