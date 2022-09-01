
from models.utils.UserMongoUtils import exist, updateUser


class LoginModel():
    def login(user):
        found = exist(user)
        return found

    def update(user, mongoUser):
        return updateUser(user, {"email": mongoUser["email"]},
                          {"$set": {"password": user["newPassword"]}})
