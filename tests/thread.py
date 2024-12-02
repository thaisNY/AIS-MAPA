import pandas as pd
import requests as r
from charset_normalizer import detect
import stomp as st

enc = None
with open(".\\..\\zomato.csv", "rb") as file:
    result = detect(file.read())
    enc = result['encoding']

dt = pd.read_csv(".\\..\\zomato.csv", encoding=enc)
send_stomp = st.Connection([('localhost', 61613)])
send_stomp.connect()
send_stomp.send(destination='/queue/server_queue', body=dt.to_json(orient="records"))