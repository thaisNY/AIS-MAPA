from time import sleep
from flask import Blueprint
import requests as r
import webbrowser as wb
import os

interface_bp = Blueprint('interface', __name__)

@interface_bp.route('/', methods=['GET', 'POST'])
def home():
    path = 'app\\views\\home.html'
    html = ''
    with open(path) as view:
        html = view.read()
    return html

@interface_bp.route('/restaurants', methods=['GET'])
def restaurant():
    path ='app\\views\\restaurants.html'
    html = ''
    with open(path) as view:
        html = view.read()
    return html

@interface_bp.route('/map', methods=["GET", "POST"])
def show_map():
    response = r.request('GET', 'http://localhost:5000/map/')
    json = response.json()
    file_path = '.\\map.html'
    retur = ''
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json['content'])
    wb.open_new_tab(file_path)
    file_path_2 = '.\\app\\views\\another_tab.html'
    with open(file_path_2, 'r', encoding='utf-8') as file_retur:
        retur = file_retur.read()
    
    return retur