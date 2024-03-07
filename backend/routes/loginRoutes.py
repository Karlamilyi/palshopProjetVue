from flask import Blueprint, jsonify, request
from flask_login import login_user, login_required, logout_user
from config import db,Login

loginRoutes = Blueprint("loginRoutes", __name__)

@loginRoutes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    user = Login.query.filter_by(email=email).first()
    if user:
        return jsonify({"message": "User Already Exists"})

    new_user = Login(email=email)  # Create a new user object
    new_user.set_password(password)  # Set password securely (e.g., using passlib)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User Created Successfully"})
