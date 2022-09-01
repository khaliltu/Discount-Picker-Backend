from configPack import mongo
from models.utils.UserUtils import clearObjects, getMail, formatAttributes
from models.utils.UserMongoUtils import registerAndNotify, updateUser


class UserModel():
    def findUserMail(token):
        return getMail(token)

    def find(email):
        return mongo.db.users.find_one({"email": email})

    def save(user):
        formatAttributes(user)
        registerAndNotify(user)
        clearObjects(user)
        return user

    def update(user, mongoUser):
        return updateUser(user, {"email": mongoUser["email"]},
                          {"$set": {"name": user["name"],
                                    "lastName": user["lastName"],
                                    "ville": user["ville"]}})
