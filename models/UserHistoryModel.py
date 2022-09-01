from configPack import mongo
from bson.objectid import ObjectId


class UserHistoryModel():
    def find(email):
        userHistory = mongo.db.histories.find({"email": email})
        return userHistory

    def add(history):
        mongo.db.histories.insert_one(history)
        return history

    def update(history):
        userHistory = mongo.db.histories.update_one(
            {"email": history["email"]}, {'$set': {"favoriteCategories": history["favoriteCategories"],
                                                   "favoriteSellers": history["favoriteSellers"],
                                                   "priceMean": history["priceMean"],
                                                   "clickNumber": history["clickNumber"]}})
        return userHistory
