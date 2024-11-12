from pymongo import MongoClient

client = MongoClient("mongodb+srv://ua16453:2NIk3tDjkSlKXZpZ@cluster0.lfksd.mongodb.net/")
db = client['Cluster0']
print("Database names:", client.list_database_names())
