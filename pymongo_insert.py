from main import get_database
import json

db = get_database()

docs = ['animales', 'cultivos', 'maquinarias', 'producciones', 'trabajadores']

for doc in docs:
  with open('./json/' + doc + '.json') as file:
    data = json.load(file)
    coleccion = db[doc]
    coleccion.insert_many(data)
    print('OK')

coleccion = db['producciones']
item_details = coleccion.find({"precio_final": {"$gt": 2500}})
for item in item_details:
  print(item["tipo"], item["cantidad"], item["calidad"], item["precio_final"], item["peso"])