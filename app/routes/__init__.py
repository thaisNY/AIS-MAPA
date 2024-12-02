from app.routes.register_restaurant import register_restaurant_bp
from app.routes.set_on_map import set_on_map_bp

def init_routes(app):
    app.register_blueprint(register_restaurant_bp, url_prefix='/register_restaurants')
    app.register_blueprint(set_on_map_bp, url_prefix='/map')
