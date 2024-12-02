from flask import jsonify, Blueprint
from app.services.generate_map import generate_map
import webbrowser as wb

set_on_map_bp = Blueprint('on_map', __name__)

@set_on_map_bp.route('/', methods=['GET'])
def show_map():
    generate_map()
    wb.open('.\\map.html',2)
    return jsonify({'message': 'Map displayed'})
