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

    def insert_records(self,request_data_temp, request_data_valv, request_data_fan, prediction_value, pue_value, it_value ):
        self.db['results'].insert_one({"tempreture": request_data_temp, "valve": request_data_valv,
                                    "fan": request_data_fan, "predicted_value": prediction_value,
                                    "it_value": it_value, "pue": pue_value,
                                    'date': datetime.datetime.now()})

        return "ok"

    def get_model(self):
        loaded_byte_model = [self.db['models'].find({})][-1]

        json_data = {}
        for i in loaded_byte_model:
            json_data = i

        print(json_data['_id'])
        pickled_model = json_data['model_obj']
        ml_model = pickle.loads(pickle.loads(pickled_model))

        return ml_model