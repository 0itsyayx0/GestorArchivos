from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def cargar_datos():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open("data.json", "w") as f:
        json.dump(datos, f, indent=4)

@app.route("/documentos", methods=["GET"])
def listar():
    return jsonify(cargar_datos())

@app.route("/documentos", methods=["POST"])
def crear():
    nuevo = request.json
    datos = cargar_datos()
    datos.append(nuevo)
    guardar_datos(datos)
    return jsonify({"mensaje": "Documento creado"}), 201

@app.route("/documentos/<id>", methods=["PUT"])
def actualizar(id):
    datos = cargar_datos()
    for doc in datos:
        if doc["id"] == id:
            doc.update(request.json)
            guardar_datos(datos)
            return jsonify({"mensaje": "Documento actualizado"})
    return jsonify({"error": "Documento no encontrado"}), 404

@app.route("/documentos/<id>", methods=["DELETE"])
def eliminar(id):
    datos = cargar_datos()
    nuevos = [doc for doc in datos if doc["id"] != id]
    guardar_datos(nuevos)
    return jsonify({"mensaje": "Documento eliminado"})

if __name__ == "__main__":
    app.run(debug=True)

print("API funcionando correctamente")
