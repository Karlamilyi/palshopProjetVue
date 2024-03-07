from flask import Blueprint, jsonify, request
from config import Login
from passlib.hash import pbkdf2_sha256
loginRoutes = Blueprint("loginRoutes", __name__)


@loginRoutes.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        hashed_password = pbkdf2_sha256.hash(password)
        if Login.find_one({"email": email}):
            return jsonify({"error": "User already exists"}), 400
        
        new_user = {
            "email": email,
            "password": hashed_password
        }
        Login.insert_one(new_user)
        return jsonify({"message": "User registered successfully"})
    except:
        return jsonify({"error": "Something went wrong"}), 500
    

@loginRoutes.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        user = Login.find_one({"email": email})
        if not user:
            return jsonify({"error": "User not found"}), 404
        if not pbkdf2_sha256.verify(password, user["password"]):
            return jsonify({"error": "Invalid password/or email"}), 400
        return jsonify({"message": "Logged in successfully"})
    except:
        return jsonify({"error": "Something went wrong"}), 500
    
    