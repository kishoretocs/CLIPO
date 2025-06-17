from pymongo import MongoClient
from app.config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
video_collection = db[MONGO_COLLECTION]
