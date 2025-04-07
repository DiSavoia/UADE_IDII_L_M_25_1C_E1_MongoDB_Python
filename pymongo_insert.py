from main import get_database
db = get_database()
collection_name = db["Produccion"]

item_1 = {
  "tipo" : "miel",
  "cantidad" : "5",
  "calidad" : "pura",
  "precio_final" : 3000,
  "peso" : "5"
}

item_2 = {
  "tipo" : "harina",
  "cantidad" : "6",
  "calidad" : "000",
  "precio_final" : 2500,
  "peso" : "150"
}


"""

Tipo 
  Huevo 
  Leche
  Carne 
  Miel 
  Lana 
  Harina
Cantidad 
Calidad 
Precio Final 
Peso 

"""

item_details = collection_name.find({"precio_final": {"$gt": 2500}})
for item in item_details:
  print(item["tipo"], item["cantidad"], item["calidad"], item["precio_final"], item["peso"])