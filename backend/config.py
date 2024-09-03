from pymongo import MongoClient
from pymongo.server_api import ServerApi

#connection string uri
client = MongoClient(uri, server_api=ServerApi("1"))
db = client.Palshop
Pals = db.paldex
Login = db.accounts
Contacts = db.contacts
