# To use database:
# pip install pymongo

import os
from dotenv import load_dotenv
import redis as r
from pymongo.mongo_client import MongoClient
import certifi # To avoid SSL Certificate Verification Error
from pymongo.server_api import ServerApi

 #Only function of this class is to take response.json and store in a MongoDB database.
    # Future: create methods in MongoDB playground to query and update user data

class DBConnection:
    def __init__(self):
        # Connect to MongoDB Atlas
        # Specify the database and collection
        self.user = os.getenv("MONGODB_USRNM")
        self.pwd = os.getenv("MONGODB_PWD")
        self.uri = f"mongodb+srv://{self.user}:{self.pwd}@cluster0.djzqswt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(self.uri, tlsCAFile=certifi.where(), server_api=ServerApi('1'))    
        self.db = self.client['Users']
        self.collection = self.db['UserInfo']

    def insert_a_user(self, user_data):
        self.collection.insert_one(user_data)
        print("Data successfully inserted!")

    ''' Needs to be re-implemented
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
        '''
    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def test_insert_user(self):
        sample_user_data = {
            "name": "Alice",
            "age": 19,
            "role": "student",
            "college": "New York University",
            "city": "New York"
        }
        self.collection.insert_one(sample_user_data)
        print("Sample user data inserted!")

    def test_redis_connection(self):
        try:
            print(redis.ping())
            print("Test Passed! Connected to Redis!")
        except Exception as e:
            print("Test failed. Failed to connect to Redis.")

#Code to run the connection test: 
#If testing 1 method, comment out the others.

#Test MongoDB
load_dotenv()
database = DBConnection()
database.test_connection()
database.test_insert_user()

#Test Redis
redis = r.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=0)
database.test_redis_connection()