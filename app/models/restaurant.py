from app.models import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    latitude = db.Column(db.String(120), unique=False, nullable=False)
    longitude = db.Column(db.String(120), unique=False, nullable=False)

    def __add_restaurant(self, name: str, latitude: str, longitude: str):
        """Adiciona um único restaurante à sessão."""
        restaurant = Restaurant(
            name=name, #type: ignore
            latitude=latitude, #type: ignore
            longitude=longitude #type: ignore
        )
        db.session.add(restaurant)
        print(f"Restaurante '{name}' adicionado com sucesso!")

    def register_restaurants(self, restaurants: list[dict]):
        """Registra múltiplos restaurantes a partir de uma lista de dicionários."""
        for rest in restaurants:
            self.__add_restaurant(
                name=rest["Restaurant Name"],
                latitude=rest["Latitude"],
                longitude=rest["Longitude"]
            )
        db.session.commit()
        print("Todos os restaurantes foram adicionados com sucesso!")
    
    def get_from_database(self, id:str|None = None):
        """Pega os valores do Banco de Dados relacionados ao atributo especificado."""
        if id != None :
            restaurant = Restaurant.query.get(id)
        else: restaurant = Restaurant.query.all()
        return restaurant