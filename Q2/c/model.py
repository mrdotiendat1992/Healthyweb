from datetime import datetime

_STANDARD_EXPIRY = 2

class Deli:
    
    def __init__(self, deliCode:str, name:str, price:float, fat:float, carbonhydrate:float, protein:float, styleOrTemp:str, url:str):
        self.deliCode = deliCode
        self.name = name
        self.price = float(price)
        self.fat = float(fat)
        self.carbonhydrate = float(carbonhydrate)
        self.protein = float(protein)
        self.url = url
        self.calories = float(self.fat * 9 + self.carbonhydrate * 4 + self.protein * 4)
        self.styleOrTemp = styleOrTemp if deliCode.startswith('C') else int(styleOrTemp)
        self.expiryhours =_STANDARD_EXPIRY

    def to_dict(self):
        return {
            "deliCode": self.deliCode,
            "name": self.name,
            "price": self.price,
            "fat": self.fat,
            "carbonhydrate": self.carbonhydrate,
            "protein": self.protein,
            "url": self.url,
            "expiryhours": self.expiryhours,
            "calories": self.calories,
            "styleOrTemp": self.styleOrTemp
        }
    
class ColdDeli:
    def __init__(self, deliCode:str, name:str, price:float, fat:float, carbonhydrate:float, protein:float, styleOrTemp:int, url:str):
        self.deliCode = deliCode
        self.name = name
        self.price = float(price)
        self.fat = float(fat)
        self.carbonhydrate = float(carbonhydrate)
        self.protein = float(protein)
        self.url = url
        self.styleOrTemp = styleOrTemp
        self.calories = float(self.fat * 9 + self.carbonhydrate * 4 + self.protein * 4)
        self.expiryhours = self.expiryHours()

    def expiryHours(self):
        if self.styleOrTemp <= 10:
            return 0.5
        elif self.styleOrTemp <= 20:
            return 1
        elif self.styleOrTemp <= 30:
            return 1.5
        else:
            return _STANDARD_EXPIRY
    
    def to_dict(self):
        return {
            "deliCode": self.deliCode,
            "name": self.name,
            "price": self.price,
            "fat": self.fat,
            "carbonhydrate": self.carbonhydrate,
            "protein": self.protein,
            "url": self.url,
            "expiryhours": self.expiryhours,
            "calories": self.calories,
            "styleOrTemp": self.styleOrTemp
        }

class HotDeli:
    _COOKING_STYLE_EXPIRY = {
        "Steaming" : 1,
        "Frying" : 3,
        "Grilling" : 1.8,
        "Roasting" : 1.5
    }

    def __init__(self, deliCode, name, price, fat, carbonhydrate, protein, styleOrTemp, url):
        self.deliCode = deliCode
        self.name = name
        self.price = float(price)
        self.fat = float(fat)
        self.carbonhydrate = float(carbonhydrate)
        self.protein = float(protein)
        self.styleOrTemp = styleOrTemp
        self.url = url
        self.calories = float(self.fat * 9 + self.carbonhydrate * 4 + self.protein * 4)
        self.expiryhours = self.expiryHours()

    def expiryHours(self):
        return type(self)._COOKING_STYLE_EXPIRY.get(self.styleOrTemp, _STANDARD_EXPIRY)
    
    def to_dict(self):
        return {
            "deliCode": self.deliCode,
            "name": self.name,
            "price": self.price,
            "fat": self.fat,
            "carbonhydrate": self.carbonhydrate,
            "protein": self.protein,
            "url": self.url,
            "expiryhours": self.expiryhours,
            "styleOrTemp": self.styleOrTemp,
            "calories": self.calories
        }
    
class User:
    def __init__(self, id:str, name:str, email:str, password:str, dob:str, handicapped:bool):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.dob = dob.split('T')[0].replace('-', '')
        self.handicapped = bool(handicapped)
        self.delisets = []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'dob': self.dob,
            'handicapped': self.handicapped,
            'delisets': self.delisets
        }
    
    def addDeli(self, deli):
        self.delisets.append(deli)

class Deliset:
    def __init__(self, deliSetName:str, deliList:list):
        self.deliSetName = deliSetName
        self.deliList = deliList

    def to_dict(self):
        return {
            'deliSetName': self.deliSetName,
            'deliList': self.deliList
        }
    
class Order:
    def __init__(self, participant:User, deliSet:Deliset, deliveryDatetime:str):
        self.participant = participant
        self.deliSet = deliSet
        self.deliveryDatetime = deliveryDatetime

    def to_dict(self):
        return {
            'participant': self.participant,
            'deliSet': self.deliSet,
            'deliveryDatetime': self.deliveryDatetime
        }
