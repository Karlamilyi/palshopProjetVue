from flask import Blueprint,jsonify
from config import db,Login

loginRoutes = Blueprint("loginRoutes", __name__)

@loginRoutes.route("/login", methods=["POST"])
