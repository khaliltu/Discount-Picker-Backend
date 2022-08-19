from itertools import product
from math import prod
from models.UserModel import UserModel
from configPack import mongo
from bson.json_util import dumps
from bson.objectid import ObjectId

from Services.scrapers.tdiscountProductScraper import getTdiscountDetails
from .utils.ProductUtils import isSubString
from Services.scrapers.jumiaProductScrapper import getJumiaDetails
from Services.scrapers.ttechProductScrapper import getTTDetails
from Services.scrapers.vongoProductScrapper import getVongoDetails


class ProductModel():
    def getAll(token):
        data, code = UserModel.find(token, cleanObjects=False)
        if (code == 200):
            products = list(mongo.db.products.find())
            data = {"products": products}
            data = dumps(data)
        return data, code

    def insert(products):
        mongo.db.products.insert_many(products)

    def deleteAll():
        try:
            mongo.db.products.delete_many({})
        except:
            print("exception")

    def getOne(token, id):
        data, code = UserModel.find(token, cleanObjects=False)
        if (code == 200):
            product = mongo.db.products.find_one({"_id": ObjectId(id)})
            registerProductDetails(product)
            data = dumps(product)
        return data, code

    def getSome(number):
        products = mongo.db.products.find().limit(number)
        data = dumps(products)
        return data, 200


def registerProductDetails(product):
    if (product["website"] == "JUMIA"):
        try:
            product["details"], product["key value details"] = getJumiaDetails(
                product["Product link"])
        except:
            pass
    if (product["website"] == "VONGO"):
        try:
            product["details"], product["key value details"] = getVongoDetails(
                product["Product link"])
        except:
            pass
    if (product["website"] == "TUNISIATECH"):
        try:
            product["details"], product["key value details"] = getTTDetails(
                product["Product link"])
        except:
            pass
    if (product["website"] == "TDISCOUNT"):
        try:
            product["details"] = getTdiscountDetails(
                product["Product link"])
            product["key value details"] = []
        except:
            pass
