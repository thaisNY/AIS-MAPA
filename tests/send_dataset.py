import pandas as pd
import requests as r
from charset_normalizer import detect

enc = None
with open(".\\..\\zomato.csv", "rb") as file:
    result = detect(file.read())
    enc = result['encoding']

dt = pd.read_csv(".\\..\\zomato.csv", encoding=enc)
post = r.post('http://127.0.0.1:5000/register_restaurants/collection', None, dt.to_json(orient="records"))
# print(post.text)