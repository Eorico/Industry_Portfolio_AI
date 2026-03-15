from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["test"]
collection = db["portfolios"]

doc = collection.find_one()
print("Full document:", doc)