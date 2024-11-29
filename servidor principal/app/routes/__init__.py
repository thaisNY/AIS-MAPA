from app.routes.register_restaurant import register_restaurant_bp

def init_routes(app):
    app.register_blueprint(register_restaurant_bp, url_prefix='/register_restaurants')
