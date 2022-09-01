from datetime import datetime, timedelta
import os
from bson import json_util
from Services.mailService import sendVerificationMail
from configPack import mongo
import json
import jwt


def registerAndNotify(user):
    user["createdAt"] = datetime.now()
    user["favoriteCategories"] = []
    user["favoriteSellers"] = []
    user["priceMean"] = []
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


def generateToken(user):
    days = int(os.environ['TOKEN_EXPIRE_DAYS'])
    exp = datetime.utcnow() + timedelta(days=days)
    encoded = jwt.encode({"email": user["email"],
                          "exp": exp}, os.environ["KEY"],
                         algorithm=os.environ["ALGORITHM"])
    return encoded
