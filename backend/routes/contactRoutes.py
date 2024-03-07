from flask import Blueprint, jsonify, request
from config import Contacts

contactRoutes = Blueprint("contactRoutes", __name__)


@contactRoutes.route("/contact", methods=["POST"])
def add_contact():
    try:
        data = request.json
        email = data.get("email")
        message = data.get("message")
        new_contact = {
            "email": email,
            "message": message
        }
        Contacts.insert_one(new_contact)
        return jsonify({"message": "Contact added successfully"})
    except:
        return jsonify({"error": "Something went wrong"}), 500
    