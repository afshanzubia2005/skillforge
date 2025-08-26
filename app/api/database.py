# To use database:
# pip install pymongo

#Only function of this class is to take response.json and store in a MongoDB database.
from pymongo import MongoClient

class DBConnection:
    def __init__(self):
        # Connect to MongoDB Atlas
        # Specify the database and collection
        self.connection_string = "mongodb+srv://no89:<8pzd1hFpG5KFqPCK>@mydatabase.x3ahw.mongodb.net/?retryWrites=true&w=majority&appName=mydatabase"
        self.client = MongoClient(self.connection_string)
        self.db = self.client("my_database")
        self.collection  = self.db["users"]
    

    def insert_a_user(self, resume):
        #resposne is sent from fastapi when it makes a call
        user_data = {
            "name": resume.get('name', ''),
            "email": resume.get('email', ''),
            "resume text": resume.get('text,' '')
        }
        self.collection.insert_one(user_data)
        print("Data successfully inserted!")        

    def close(self):
        self.client.close()

    def get_last_parsed(self):
        return self.collection.find_one(sort=[('_id', -1)])