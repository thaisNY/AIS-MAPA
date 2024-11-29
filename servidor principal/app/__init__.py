from flask import Flask
from app.routes import init_routes

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config.from_object('app.config.Config')

    # Inicializar rotas
    init_routes(app)

    return app
