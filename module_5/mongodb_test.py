from pymongo import MongoClient

db_url = 'mongodb+srv://admin:admin@cluster0.zpn7y.mongodb.net/?retryWrites=true&w=majority' # or some other default url
client = MongoClient(db_url)
db=client.pytech

print(client.list_database_names())

print(db.list_collection_names())
