from main import get_database

db = get_database()

# Busqueda de productos
coleccion = db['producciones']
docs = coleccion.find({"precio_final": {"$gt": 2500}})
print('\nProductos cuyo precio final es mayor a 2500 pesos')
for doc in docs:
  print(doc)

doc = coleccion.find({"tipo": 'miel', 'calidad': '000'})
for i,item in enumerate(doc):    
    print(str(i+1) + 
          "- Cantidad: " + str(item["cantidad"]) + 
          ", precio_final: " + str(item["precio_final"]) + 
          ", peso: " + str(item["peso"]) + 
          ", fecha_ingreso: " + 
          str(item["fecha_ingreso"]))

# Busqueda de animales
coleccion = db['animales']
docs = coleccion.find({"tipo": "abeja", "peso": { "$gt": 20 }})
print('\nAbejas cuyo peso es mayor a 20 KG\n')
for i, doc in enumerate(docs):
    print(str(i+1) + "- Tipo: " + str(doc["tipo"]) + 
          ", peso: " + str(doc["peso"]) + 
          ", genero: " + str(doc["genero"]) + 
          ", edad: " + str(doc["edad"]))

docs = coleccion.find({"tipo": "oveja", "genero": "hembra"})
print('\nOvejas hembras\n')
for doc in docs:
    print(doc)

# Busqueda de cultivos

# Busqueda de maquinarias
coleccion = db['maquinarias']
docs = coleccion.find({"Mantenimiento": True})
print('\nMaquinarias que necesitan mantenimiento\n')
for i, doc in enumerate(docs):
    print(str(i+1) + "- Nombre: " + str(doc["Nombre"]) + 
          ", marca: " + str(doc["Marca"]) + 
          ", tipo: " + str(doc["Tipo"]) + 
          ", mantenimiento: " + str(doc["Mantenimiento"]) + 
        ", fecha ultima reparación: " + str(doc["Fecha Ultima Reparación"]) + 
        ", fecha ultima revisión: " + str(doc["Fecha Ultima Revisión"]) + 
        ", precio: " + str(doc["Precio"]) + 
        ", capacidad de combustible: " + str(doc["Capacidad de Combustible"]))