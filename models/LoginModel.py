from datetime import datetime, timedelta
import json
import jwt
import os
from models.UserModel import exist
from werkzeug.security import check_password_hash


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


def generateToken(user):
    days = int(os.environ['TOKEN_EXPIRE_DAYS'])
    exp = datetime.utcnow() + timedelta(days=days)
    encoded = jwt.encode({"email": user["email"],
                          "exp": exp}, os.environ["KEY"],
                         algorithm=os.environ["ALGORITHM"])
    return encoded
