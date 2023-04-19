import json
import pandas as pd


lijekovi = pd.read_excel('C:/Users/Toni/Documents/Python/Učenje/Projekt/myapp/lijekovi.xlsx')
lijekovi_json = lijekovi.to_json()
print(lijekovi_json)

with open('samolijecenje.json', 'w') as sjson:
    json.dump(lijekovi_json, sjson, indent=2)

