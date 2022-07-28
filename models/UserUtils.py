import jwt
import os
from werkzeug.security import generate_password_hash


def formatAttributes(user, update=False):
    if not update:
        user["password"] = generate_password_hash(user["password"])
        user["email"] = user["email"].lower()
        user["name"] = user["name"].lower().capitalize()
        user["lastName"] = user["lastName"].lower().capitalize()
        user["ville"] = user["ville"].lower().capitalize()
    else:
        user["newPassword"] = generate_password_hash(user["newPassword"])


def clearObjects(user):
    del user['_id']
    del user['createdAt']
    del user["password"]


def getMail(token):
    try:
        decoded = jwt.decode(
            token, os.environ['KEY'],
            algorithms=os.environ["ALGORITHM"])
        return decoded["email"]
    except:
        return ""
