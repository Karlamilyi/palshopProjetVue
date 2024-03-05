from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId  # Import ObjectId from bson module
from flask import Flask, request, jsonify
import random

uri = "mongodb+srv://Beuhnnyto:obcMfdkwnb4FVLph@beuhnnyto.tvogdgo.mongodb.net/?retryWrites=true&w=majority&appName=Beuhnnyto"

client = MongoClient(uri, server_api=ServerApi("1"))
db = client.Palshop
collection = db.paldex
total_count = collection.count_documents({})

app = Flask(__name__)


@app.route("/pals", methods=["GET"])
def get_all():
    data = collection.find()
    data = {
        str(item["key"]): {
            "name": item["name"],
            "price": item["price"],
            "image": item["image"],
        }
        for item in data
    }
    return jsonify(data)


@app.route("/pals/<name>", methods=["GET"])
def get_one(name):
    try:
        data = collection.find_one({"name": name})
        data = {
            str(data["key"]): {
                "name": data["name"],
                "price": data["price"],
                "image": data["image"],
            }
        }
        return jsonify(data)
    except:
        return jsonify({"error": "Not found"}), 404


@app.route("/accueil", methods=["GET"])
# gets 3 random items from the database


def get_accueil():
    random_indices = random.sample(range(total_count), 3)
    random_items = collection.find().limit(3).skip(random_indices[0])

    data = {
        str(item["key"]): {
            "name": item["name"],
            "price": item["price"],
            "image": item["image"],
        }
        for item in random_items
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
