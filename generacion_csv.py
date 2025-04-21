from main import get_database
import pandas as pd

db = get_database()


# Consulta Miel calidad 000
coleccion = db['producciones']

doc = list(coleccion.find({"tipo": 'miel', 'calidad': '000'}))
df = pd.DataFrame(doc)
df.to_csv("miel_mal_cargada.csv", index=False)
print('OK')

# Productos con precio mayor a 2500
coleccion = db['producciones']

doc = list(coleccion.find({"precio_final": {"$gt": 2500}}))
df = pd.DataFrame(doc)
df.to_csv("precio_mayor_2500.csv", index=False)
print('OK')

# Abejas con peso mayor a 20kg
coleccion = db['animales']

doc = list(coleccion.find({"tipo": "abeja", "peso": { "$gt": 20 }}))
df = pd.DataFrame(doc)
df.to_csv("abejas_pesadas.csv", index=False)
print('OK')

# Ovejas hembras
coleccion = db['animales']

doc = list(coleccion.find({"tipo": "oveja", "genero": "hembra"}))
df = pd.DataFrame(doc)
df.to_csv("ovejas_hembras.csv", index=False)
print('OK')

# Maquinarias que necesitan mantenimiento
coleccion = db['Maquinarias']
doc = list(coleccion.find({"Mantenimiento": True}))
df = pd.DataFrame(doc)
df.to_csv("maquinas_a_reparar.csv", index=False)
print('OK')

# Cultivos saludables con producción mayor a 300
coleccion = db['cultivos']
doc = list(coleccion.find({"estado_salud": "Saludable", "produccion_estimada": {"$gt":300}}))
df = pd.DataFrame(doc)
df.to_csv("cultivos_sanos_300.csv", index=False)
print('OK')