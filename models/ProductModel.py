from configPack import mongo
from bson.json_util import dumps
from bson.objectid import ObjectId


class ProductModel():
    def getAll():
        products = list(mongo.db.products.find())
        return products

    def insert(products):
        mongo.db.products.insert_many(products)

    def deleteAll():
        try:
            mongo.db.products.delete_many({})
        except:
            print("exception")

    def getOne(id):
        product = mongo.db.products.find_one({"_id": ObjectId(id)})
        return product

    def getSome(number):
        products = mongo.db.products.find().limit(number)
        data = dumps(products)
        return data, 200
