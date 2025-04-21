from flask import Flask, jsonify 
from pymongo import MongoClient 

app = Flask(__name__) 
# Conexión con MongoDB 
client = MongoClient("mongodb://localhost:27017/") 
db = client["GranjaMongo"] 

@app.route('/cultivos', methods=['GET']) 
def get_cultivos(): 
    cultivos = db["cultivos"] 
    data = list(cultivos.find({}, {"_id": 0}))
    return jsonify(data) 
 
@app.route('/trabajadores', methods=['GET'])
def get_trabajadores():
    trabajadores = db["trabajadores"]
    data = list(trabajadores.find({}, {"_id": 0}))
    return jsonify(data)

@app.route('/animales', methods=['GET'])
def get_animales():
    animales = db["animales"]
    data = list(animales.find({}, {"_id": 0}))
    return jsonify(data)

@app.route('/maquinarias', methods=['GET'])
def get_maquinarias():
    maquinarias = db["Maquinarias"]
    data = list(maquinarias.find({}, {"_id": 0}))
    return jsonify(data)

@app.route('/producciones', methods=['GET'])
def get_producciones():
    producciones = db["producciones"]
    data = list(producciones.find({}, {"_id": 0}))
    return jsonify(data)

if __name__ == '__main__': 
    app.run(debug=True)