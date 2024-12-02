import h3
from flask import jsonify
from app.models.restaurant import Restaurant
import plotly.express as px
import os

def generate_map():
    # Obtém lista de restaurantes do banco de dados
    rest = Restaurant()
    rest_list = rest.get_from_database()
    geojson_features = []

    for rest in rest_list:  # type: ignore
        # Converta a latitude e longitude do restaurante para um índice H3
        h3_index = h3.latlng_to_cell(float(rest.latitude), float(rest.longitude), res=int(os.getenv('MAP_HEXES_RESOLUTION', 4)))
        
        # Obtenha os vértices do hexágono
        hexagon_boundary = [[lon, lat] for lat, lon in h3.cell_to_boundary(h3_index)]

        # Formate o polígono GeoJSON para visualização no mapa
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [hexagon_boundary]
            },
            "properties": {
                "name": rest.name,  # Propriedade exemplo
            },
        }
        geojson_features.append(feature)

    # GeoJSON FeatureCollection
    geojson = {
        "type": "FeatureCollection",
        "features": geojson_features,
    }

    # Calcular o centro do mapa
    center_lat = sum([float(rest.latitude) for rest in rest_list]) / len(rest_list) # type: ignore
    center_lon = sum([float(rest.longitude) for rest in rest_list]) / len(rest_list) # type: ignore

    # Criar lista de identificadores e valores de cor
    loc = [f"{featu['properties']['name']}" for featu in geojson_features]
    # col = [n for n in range(1, len(geojson_features) + 1)]
    
    # Criar o mapa
    fig = px.choropleth_mapbox(
        geojson=geojson,  # GeoJSON dos polígonos
        featureidkey="properties.name",  # Chave para identificação das propriedades
        locations=loc,
        color_continuous_scale="Viridis",  # Escala de cores
        mapbox_style="carto-positron",  # Estilo do mapa
        center={"lat": center_lat, "lon": center_lon},  # Centro do mapa
        zoom=4,  # Ajustar zoom
        opacity=0.9,  # Transparência dos polígonos
    )

    # Mostrar o mapa
    # fig.show()
    
    with open("map.html", "w", encoding='utf-8') as map_file:
        map_file.write(fig.to_html())

    return jsonify({'message': 'Map generated'})
