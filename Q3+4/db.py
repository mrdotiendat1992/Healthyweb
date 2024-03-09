from pymongo import MongoClient

client = MongoClient('localhost', 27017)

from model import User, HotDeli, ColdDeli, Deliset, Order

from _env import *

db = client.get_database(DB_NAME)

def create_user(id:str, name:str, email:str, password:str, dob:str, handicapped:bool):
    try:
        user = User(id, name, email, password, dob, handicapped)
        exists = db.get_collection(USER_COLLECTION_NAME).find_one({'email': email})
        if exists:
            return False
        else:
            newuser = db.get_collection(USER_COLLECTION_NAME).insert_one(user.to_dict())
            if newuser:
                return db.get_collection(USER_COLLECTION_NAME).find_one({'email': email})
    except:
        return False
    
def create_deli(deliCode:str, name:str, price:float, fat:float, carbonhydrate:float, protein:float, styleOrTemp:str, url:str):
    try:
        if deliCode.startswith('H'):
            if not db.get_collection(HOT_DELI_COLLECTION_NAME).find_one({'deliCode': deliCode}):
                deli = HotDeli(deliCode, name, price, fat, carbonhydrate, protein, styleOrTemp, url)
                if not db.get_collection(HOT_DELI_COLLECTION_NAME).insert_one(deli.to_dict()):
                    return False
            else:
                return False
        elif deliCode.startswith('C'):
            if not db.get_collection(COLD_DELI_COLLECTION_NAME).find_one({'deliCode': deliCode}):
                deli = ColdDeli(deliCode, name, price, fat, carbonhydrate, protein, int(styleOrTemp), url)
                if not db.get_collection(COLD_DELI_COLLECTION_NAME).insert_one(deli.to_dict()):
                    return False
            else:
                return False
        else:
            return False
        newdeli = db.get_collection(DELI_COLLECTION_NAME).insert_one(deli.to_dict())
        if newdeli:
            return db.get_collection(DELI_COLLECTION_NAME).find_one({'deliCode': deliCode})
    except Exception as e:
        print(e)
        return False

def get_delis():
    try:
        delis = db.get_collection(DELI_COLLECTION_NAME).find()
        if delis:
            return delis
        return None
    except:
        return None

def create_deliset(name:str, deliList:list):
    try:
        deliset = Deliset(name, deliList)
        if not db.get_collection(DELISET_COLLECTION_NAME).find_one({'name': name}):
            newdeliset = db.get_collection(DELISET_COLLECTION_NAME).insert_one(deliset.to_dict())
            if newdeliset:
                return db.get_collection(DELISET_COLLECTION_NAME).find_one({'name': name})
            else:
                return False
        else:
            return False
    except:
        return False

def create_order(participant, name, datetimeDelivery):
    try:
        deliset = db.get_collection(DELISET_COLLECTION_NAME).find_one({'name': name})
        datetimeDelivery = datetimeDelivery.replace('T', ' ')
        order = Order(participant, deliset, datetimeDelivery)
        neworder = db.get_collection('orders').insert_one(order.to_dict())
        if neworder:
            return neworder
        else:
            return False
    except:
        return False

