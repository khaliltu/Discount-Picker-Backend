from datetime import datetime
from bson import json_util
from Services.mailService import sendVerificationMail
from configPack import mongo
import json


def registerAndNotify(user):
    user["createdAt"] = datetime.now()
    user["favoriteCategories"] = []
    mongo.db.users.insert_one(user)
    sendVerificationMail(user["email"], user["name"])


def exist(user):
    try:
        search = mongo.db.users.find_one({"email": user["email"].lower()})
        search = json.loads(json_util.dumps(search))
        return search
    except:
        return []


def updateUser(newUser, filter, newValues):
    filter = filter
    newValues = newValues
    try:
        mongo.db.users.update_one(filter, newValues)
        data, code = {"user": newUser}, 200
    except:
        data, code = {
            "message": "erreur lors de la connection à la base de données"}, 503
    return data, code
