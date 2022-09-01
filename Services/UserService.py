

import json
from models.UserModel import UserModel
from models.utils.UserMongoUtils import exist
from models.utils.UserUtils import clearObjects
from bson import json_util


class UserService():
    def find(token, cleanObjects=True):
        email = UserModel.findUserMail(token)
        if(email):
            try:
                user = UserModel.find(email)
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
        if (not exist(user)):
            try:
                user = UserModel.save(user)
                data, code = json.dumps(user), 200
            except:
                data = {"message": "un probleme est survenue lors de l'inscription"}
                data, code = json.dumps(data), 503
        else:
            data = {"message": user["email"] + " existe deja!"}
            data, code = json.dumps(data), 409
        return data, code

    def update(token, user):
        data, code = UserService.find(token)
        if code == 200:
            mongoUser = json.loads(data)['user']
            data, code = UserModel.update(user, mongoUser)
            data = json.dumps(data)
            return data, code
        return data, code
