from flask import Blueprint, jsonify, request
from app.services.tokens_service import jwt_required
from app.crud.base_crud import read_json, write_json
import os

DATA_FILE = os.getenv("DATA_FILE", "data.json")

documentos_bp = Blueprint("documentos", __name__, url_prefix="/documentos")

@documentos_bp.route("/", methods=["GET"])
@jwt_required()
def listar():
    return jsonify(read_json(DATA_FILE))

@documentos_bp.route("/", methods=["POST"])
@jwt_required(roles=["admin", "editor"])
def crear():
    nuevo = request.get_json()
    datos = read_json(DATA_FILE)
    datos.append(nuevo)
    write_json(DATA_FILE, datos)
    return jsonify({"mensaje": "Documento creado"}), 201
