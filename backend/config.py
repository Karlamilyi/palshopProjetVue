from pymongo import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://Beuhnnyto:ARISestUNhumainWallah@beuhnnyto.tvogdgo.mongodb.net/?retryWrites=true&w=majority&appName=Beuhnnyto"
client = MongoClient(uri, server_api=ServerApi("1"))
db = client.Palshop
Pals = db.paldex
Login = db.accounts
Contacts = db.contacts
