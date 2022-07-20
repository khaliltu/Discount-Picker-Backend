

from json import dumps
import json
from bson import json_util
from flask_restful import Resource
from models.UserModel import UserModel
from flask import request, Response


class UserService(Resource):
    def get(self):
        users = UserModel.getAll()
        return dumps(users, default=json_util.default)

    def post(self):
        user = json_util.loads(json_util.dumps(request.json))
        data, code = UserModel.save(user)
        return Response(data, status=code, mimetype='application/json')
