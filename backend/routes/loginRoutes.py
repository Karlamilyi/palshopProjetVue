import email
from flask import Blueprint, jsonify, request
from flask_login import login_user, login_required, logout_user
from config import db,Login

loginRoutes = Blueprint("loginRoutes", __name__)

@loginRoutes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    print(data)