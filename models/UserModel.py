from datetime import datetime
from bson import json_util
import json
from configPack import mongo
from Services.mailService import sendVerificationMail


class UserModel():
    def getAll():
        users = list(mongo.db.users.find())
        return users

    def save(user):
        search = mongo.db.users.find({"email": user["email"]})
        search = json.loads(json_util.dumps(search))
        if (search == []):
            try:
                registerAndNotify(user)
                del user['_id']
                del user['createdAt']
                data, code = json.dumps(user), 200
            except:
                data = {"message": "un probleme est survenue lors de l'inscription"}
                data, code = json.dumps(data), 504
        else:
            data = {"message": user["email"] + " existe deja!"}
            data, code = json.dumps(data), 409
        return data, code


def registerAndNotify(user):
    user["createdAt"] = datetime.now()
    user["favoriteCategories"] = []
    mongo.db.users.insert_one(user)
    sendVerificationMail(user["email"], user["name"])
