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


@catalogRoutes.route("/pals/<key>", methods=["GET"])
def get_one(key):
    try:
        data = Pals.find_one({"key": key})
        data = {
            "name": data["name"],
            "price": data["price"],
            "image": data["image"],
            "description": data["description"],
            "suitability": data["suitability"],
            "types": data["types"],
        }
        return jsonify(data)
    except:
        return jsonify({"message": "Not found"}), 404
