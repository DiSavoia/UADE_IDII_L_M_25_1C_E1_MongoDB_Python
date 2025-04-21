from main import get_database
from auto_gen import *
#import json

db = get_database()

# Insercion por JSON
'''
docs = ['animales', 'cultivos', 'maquinarias', 'producciones', 'trabajadores']

for doc in docs:
  with open('./json/' + doc + '.json') as file:
    data = json.load(file)
    coleccion = db[doc]
    coleccion.insert_many(data)
    print('OK')
'''

# Documentos de producciones
coleccion = db['producciones']
datos = generar_productos(50)
coleccion.insert_many(datos)

# Documentos de animales
coleccion = db['animales']
datos = generar_animales(50)
coleccion.insert_many(datos)

# Documentos de cultivos
coleccion = db['cultivos']
datos = generar_cultivos(50)
coleccion.insert_many(datos)

# Documentos de maquinarias
coleccion = db['maquinarias']
datos = generar_maquinarias(50)
coleccion.insert_many(datos)

# Documentos de trabajadores
coleccion = db['trabajadores']
datos = generar_trabajadores(50)
coleccion.insert_many(datos)
