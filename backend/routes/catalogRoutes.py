from flask import Blueprint, jsonify
from config import Pals

catalogRoutes = Blueprint("catalogRoutes", __name__)


@catalogRoutes.route("/pals", methods=["GET"])
def get_all():
    data = Pals.find()
    data = {
        str(item["key"]): {
            "name": item["name"],
            "price": item["price"],
            "image": item["image"],
        }
        for item in data
    }
    return jsonify(data)


@catalogRoutes.route("/pals/<name>", methods=["GET"])
def get_one(name):
    try:
        data = Pals.find_one({"name": name})
        data = {
            str(data["key"]): {
                "name": data["name"],
                "price": data["price"],
                "image": data["image"],
                "description": data["description"],
                "suitability": data["suitability"],
                
            }
        }
        return jsonify(data)
    except:
        return jsonify({"error": "Not found"}), 404