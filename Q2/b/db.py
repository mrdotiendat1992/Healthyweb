from pymongo import MongoClient

client = MongoClient('localhost', 27017)

from model import User, HotDeli, ColdDeli

def create_user(id:str, name:str, email:str, password:str, dob:str, handicapped:bool):
    try:
        user = User(id, name, email, password, dob, handicapped)
        exists = client.get_database('db').get_collection('users').find_one({'email': email})
        if exists:
            return False
        else:
            newuser = client.get_database('db').get_collection('users').insert_one(user.to_dict())
            if newuser:
                return newuser
    except:
        return False
        
def get_user(email):
    try:
        user = client.get_database('db').get_collection('users').find_one({'email': email})
        if user:
            return user
        return None
    except:
        return None
    
def create_deli(deliCode:str, name:str, price:float, fat:float, carbonhydrate:float, protein:float, storagetemporstyle:str, url:str):
    try:
        if deliCode.startswith('H'):
            deli = HotDeli(deliCode, name, price, fat, carbonhydrate, protein, storagetemporstyle, url)
            if not client.get_database('db').get_collection('hotdelis').insert_one(deli.to_dict()):
                print("Failed")
        elif deliCode.startswith('C'):
            deli = ColdDeli(deliCode, name, price, fat, carbonhydrate, protein, int(storagetemporstyle), url)
            if not client.get_database('db').get_collection('colddelis').insert_one(deli.to_dict()):
                print("Failed")
        else:
            return False
        newdeli = client.get_database('db').get_collection('delis').insert_one(deli.to_dict())
        if newdeli:
            return True
    except Exception as e:
        print(e)
        return False

def get_delis():
    try:
        delis = client.get_database('db').get_collection('delis').find()
        if delis:
            return delis
        return None
    except:
        return None

def upload_delis(file):
    f = open(file, 'r', encoding='utf-8')
    for x in f.readlines():
        data = x.split(',')
        create_deli(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])

def upload_users(file):
    f = open(file, 'r', encoding='utf-8')
    for x in f.readlines():
        data = x.split(',')
        create_user(data[0], data[1], data[4].strip(), "123", data[2], data[3])
