from pymongo import MongoClient

client = MongoClient('mongodb+srv://verasantiwijayaa:s3WNDPpdhS3g7xIX@cluster0.yuyn0jm.mongodb.net/test')

mydb = client["Nama_Database"]
mycol = mydb["my_collection"]
role = mydb["Privilege_Login"]