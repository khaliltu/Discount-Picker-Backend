import json
from Services.UserService import UserService
from models.LoginModel import LoginModel
from werkzeug.security import check_password_hash
from models.utils.UserMongoUtils import generateToken

from models.utils.UserUtils import formatAttributes


class LoginService():
    def login(user):
        found = LoginModel.login(user)
        if (not found):
            data = {"message": user["email"] +
                    " ne coresspend à aucun utilisateur!"}
            data, code = json.dumps(data), 401
        else:
            if not check_password_hash(found["password"], user["password"]):
                data = {"message": "mot de passe incorrect"}
                data, code = json.dumps(data), 403
            else:
                token = generateToken(user)
                userName = found["name"]+" "+found["lastName"]+" "
                data = {"token": token,
                        "userName": userName}
                data, code = json.dumps(data), 200
        return data, code

    def update(token, user):
        data, code = UserService.find(token, cleanObjects=False)
        if code == 200:
            mongoUser = data
            if not check_password_hash(mongoUser["password"], user["password"]):
                data, code = json.dumps(
                    {"message": "mot de passse incorrect"}), 401
            else:
                formatAttributes(user, update=True)
                data, code = LoginModel.update(user, mongoUser)
                data = json.dumps(data)
        return data, code
