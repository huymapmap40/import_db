import json
from pymongo import MongoClient
from constantdb.database import MONGO_URI
from models.general_info import GeneralInfo
from models.brand import Brand
from models.item_specification import ItemSpecification
from models.motor_model import MotorModel
from handling.util import Util

try:
    conn = MongoClient(MONGO_URI)
    print("Connect mongo db sucessful.")
except:
    print("Cannot connect to mongo db.")

db = conn.MotorSpecification
manufacturerCollection = db.manufacturer
# allBrand = manufacturerCollection.find()
# for item in allBrand:
#     print({"id":str(item["_id"]), "brand": item["brand"]})

generalInfoObj = GeneralInfo("avatar link", "description model x", ["image1", "image 2"], 
                                ["videos 1"], "logo link", "bronx 975")

itemMakeModel = ItemSpecification("make model", "harley")
itemCapacity = ItemSpecification("capacity", "50 litre")
itemSeatHeigh = ItemSpecification("Seat Height", "850mm")
listItemSpecification = [itemMakeModel.__dict__, itemCapacity.__dict__, itemSeatHeigh.__dict__]
itemMaxSpeed = ItemSpecification("max speed", "299km/h")
itemMaxtorque = ItemSpecification("max torque", "500Nm")
listItemSpecsDucati = [itemMaxSpeed.__dict__, itemMaxtorque.__dict__]

motorModelObj = MotorModel("harly-davision", "description harley", "main_image model", specifications=listItemSpecification)
motorModelOtherObj = MotorModel("Ducati", "vip rich max", "Link main image ducati here", ["image 0"], specifications=listItemSpecsDucati)
listModels = [motorModelObj.__dict__, motorModelOtherObj.__dict__]
brandObject = Brand(generalInfoObj.__dict__, listModels)
# documentToInsert = Util.parseObject2Dict(brandObject)

manufacturerCollection.insert_one({"brand":brandObject.__dict__})
print("=========> Done")
