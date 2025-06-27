from pymongo import MongoClient
from bson import ObjectId
from app.config import Config

class User:
    def __init__(self):
        self.client= MongoClient(Config.MONGO_URI)
        self.db=self.client.get_database()
        self.collection=self.db.users

    def create(self,data):
        if not all(key in data for key in ["name","email","password"]):
            raise ValueError("Missing fields required")
        result=self.collection.insert_one(data)
        return str(result.inserted_id)
        
    def get_all(self):
        users=self.collection.find()
        return[
            {**user,"_id": str(user["_id"])} for user in users
        ]
    def get_by_id(self,user_id):
        user=self.collection.find_one({"_id":ObjectId(user_id)})
        if user:
            return{**user,"_id": str(user["_id"])}
        return None
        
    def update(self,user_id,data):
        if not data:
            raise ValueError("No Data Provided")
        result=self.collection.update_one(
            {"_id":ObjectId(user_id)},{"$set":data}
        )
        return result.modified_count > 0
        
    def delete(self,user_id):
        result=self.collection.delete_one({"_id":ObjectId(user_id)})
        return result.deleted_count >0