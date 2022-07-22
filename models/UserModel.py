from datetime import datetime
from bson import json_util
import json
from configPack import mongo
from Services.mailService import sendVerificationMail
from werkzeug.security import generate_password_hash


class UserModel():
    def save(user):
        formatAttributes(user)
        if (not exist(user)):
            try:
                registerAndNotify(user)
                clearObjects(user)
                data, code = json.dumps(user), 200
            except:
                data = {"message": "un probleme est survenue lors de l'inscription"}
                data, code = json.dumps(data), 503
        else:
            data = {"message": user["email"] + " existe deja!"}
            data, code = json.dumps(data), 409
        return data, code


def registerAndNotify(user):
    user["createdAt"] = datetime.now()
    user["favoriteCategories"] = []
    mongo.db.users.insert_one(user)
    sendVerificationMail(user["email"], user["name"])


def formatAttributes(user):
    user["password"] = generate_password_hash(user["password"])
    user["email"] = user["email"].lower()
    user["name"] = user["name"].lower().capitalize()
    user["lastName"] = user["lastName"].lower().capitalize()
    user["ville"] = user["ville"].lower().capitalize()


def exist(user):
    try:
        search = mongo.db.users.find_one({"email": user["email"]})
        search = json.loads(json_util.dumps(search))
        return search
    except:
        return []


def clearObjects(user):
    del user['_id']
    del user['createdAt']
