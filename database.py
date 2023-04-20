from pymongo import MongoClient


MONGO_URI = 'mongodb://localhost:27017/'


def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        db = client["ProductsDB"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
