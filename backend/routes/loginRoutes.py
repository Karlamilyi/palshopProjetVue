from flask import Blueprint, jsonify, request
from flask_login import login_user, login_required, logout_user
from config import db, User  # Replace with your user model name (e.g., Login)
from forms import LoginForm  # Import your LoginForm from forms.py

loginRoutes = Blueprint("loginRoutes", __name__)


@loginRoutes.route("/login", methods=["POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            return jsonify({"message": "Login Successful"})
        else:
            return jsonify({"message": "Invalid Credentials"})
    return jsonify({"message": "Invalid Form Data"}), 400  # Handle bad form data


@loginRoutes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"message": "User Already Exists"})

    new_user = User(email=email)  # Create a new user object
    new_user.set_password(password)  # Set password securely (e.g., using passlib)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User Created Successfully"})
