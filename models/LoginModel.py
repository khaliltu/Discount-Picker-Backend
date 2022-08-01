from datetime import datetime, timedelta
import json
import jwt
import os
from werkzeug.security import check_password_hash
from models.UserMongoUtils import exist, updateUser
from models.UserModel import UserModel
from models.UserUtils import formatAttributes


class LoginModel():
    def login(user):
        found = exist(user)
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
        data, code = UserModel.find(token, cleanObjects=False)
        if code == 200:
            print(user)
            mongoUser = data
            if not check_password_hash(mongoUser["password"], user["password"]):
                data, code = json.dumps(
                    {"message": "mot de passse incorrect"}), 401
            else:
                formatAttributes(user, update=True)
                data, code = updateUser(user, {"email": mongoUser["email"]},
                                        {"$set": {"password": user["newPassword"]}})
                data = json.dumps(data)
        return data, code


def generateToken(user):
    days = int(os.environ['TOKEN_EXPIRE_DAYS'])
    exp = datetime.utcnow() + timedelta(days=days)
    encoded = jwt.encode({"email": user["email"],
                          "exp": exp}, os.environ["KEY"],
                         algorithm=os.environ["ALGORITHM"])
    return encoded
