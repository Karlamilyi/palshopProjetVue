from flask import Blueprint, jsonify
from config import db,Pals
import random

homeRoutes = Blueprint("homeRoutes", __name__)



@homeRoutes.route("/accueil", methods=["GET"])
def get_accueil():
    total_count = Pals.count_documents({})
    random_indices = random.sample(range(total_count), 3)
    random_items = Pals.find().limit(3).skip(random_indices[0])

    data = {
        str(item["key"]): {
            "name": item["name"],
            "price": item["price"],
            "image": item["image"],
        }
        for item in random_items
    }
    return jsonify(data)