from flask_pymongo import pymongo
from dotenv import load_dotenv
import os
import datetime
import pickle
import datetime

class Mongo_db_repository:

    def __init__(self):
        self.client = pymongo.MongoClient({os.environ.get("DATABASE")})
        self.db = self.client['airconditionerDb']

    def insert_records(self, data):
        self.db['test'].insert_one({"tempreture": data['tempreture'], "valve": data['valve'],
                                    "fan": data['fan'], "predicted_value": data['predicted_value'],
                                    "real_value":data['real_value'], 'date': datetime.datetime.now()})

        return "ok"