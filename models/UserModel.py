import json
from configPack import mongo
from models.UserUtils import clearObjects, getMail, formatAttributes
from models.UserMongoUtils import exist, registerAndNotify, updateUser
from bson import json_util


class UserModel():
    def find(token, cleanObjects=True):
        email = getMail(token)
        if(email):
            try:
                user = mongo.db.users.find_one({"email": email})
                if not cleanObjects:
                    user = json.loads(json_util.dumps(user))
                    return user, 200
                clearObjects(user)
                data = {"user": user}
                data, code = json.dumps(data), 200
            except:
                data = {"message": "un probleme est survenu"}
                data, code = json.dumps(data), 503
        else:
            data = {"message": "invalid access token"}
            data, code = json.dumps(data), 401
        return data, code

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

    def update(token, user):
        data, code = UserModel.find(token)
        if code == 200:
            mongoUser = json.loads(data)['user']
            print(mongoUser)
            print(user)
            data, code = updateUser(user, {"email": mongoUser["email"]},
                                    {"$set": {"name": user["name"],
                                              "lastName": user["lastName"],
                                              "ville": user["ville"]}})
            data = json.dumps(data)
            return data, code
        return data, code
