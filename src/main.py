from pymongo import MongoClient
from constantdb.database import MONGO_URI

try:
    conn = MongoClient("mongodb://motorspecifications:P%40ssw0rd@clusterpythonnew-shard-00-00-wthjc.gcp.mongodb.net:27017,clusterpythonnew-shard-00-01-wthjc.gcp.mongodb.net:27017,clusterpythonnew-shard-00-02-wthjc.gcp.mongodb.net:27017/MotorSpecification?ssl=true&replicaSet=ClusterPythonNew-shard-0&authSource=admin&retryWrites=true&w=majority")
    # conn = MongoClient(MONGO_URI)
    print("Connect mongo db sucessful.")
except:
    print("Cannot connect to mongo db.")

db = conn.MotorSpecification
manufacturerCollection = db.manufacturer
allBrand = manufacturerCollection.find()
for item in allBrand:
    print({"id":str(item["_id"]), "brand": item["brand"]})
print("Done")
