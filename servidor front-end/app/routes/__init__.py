from app.routes.interface import interface_bp

def init_routes(app):
    app.register_blueprint(interface_bp, url_prefix='/app')