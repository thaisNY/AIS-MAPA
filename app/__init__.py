from flask import Flask
from app.routes import init_routes
from app.models import init_models

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config.from_object('app.config.Config')

    # Inicializar rotas
    with app.app_context():
        init_routes(app)
    
    with app.app_context():
        init_models(app)

    return app
