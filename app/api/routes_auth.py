from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, login_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    body = request.get_json()
    email = body.get("email")
    password = body.get("password")
    roles = body.get("roles", ["user"])
    resp, code = register_user(email, password, roles)
    return jsonify(resp), code

@auth_bp.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    email = body.get("email")
    password = body.get("password")
    resp, code = login_user(email, password)
    return jsonify(resp), code
