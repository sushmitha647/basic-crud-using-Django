from pymongo import MongoClient
client=MongoClient("mongodb+srv://sushmithakumarsk:Sush%401928@cluster0.kus9qc1.mongodb.net/")
db=client["datas"]
col=db["users"]