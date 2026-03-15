from pymongo import MongoClient
from typing import Optional, Dict

class Repositories: 
    def __init__(self, mongo_uri: str, db_name: str = "test"):
        self.client  = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db["portfolios"]
        
    def get_portfolio(self) -> Optional[Dict]:
        return self.collection.find_one()