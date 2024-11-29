from flask import Blueprint, request, jsonify

register_restaurant_bp = Blueprint('register', __name__)

def register(data: dict):
    pass

@register_restaurant_bp.route('/', methods=['GET'])
def register_new_geolocation():
    # registra uma nova localização
    return jsonify({'message': 'List of users'})

@register_restaurant_bp.route('/collection', methods=['POST'])
def register_collection():
    if request.is_json():
        collec = request.get_json()
        for item in collec:
            register({
                "":""
            })