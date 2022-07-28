
from bson import json_util
from flask_restful import Resource
from models.UserModel import UserModel
from flask import request, Response


class UserService(Resource):
    def get(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        data, code = UserModel.find(token)
        return Response(data, status=code, mimetype='application/json')

    def post(self):
        user = json_util.loads(json_util.dumps(request.json))
        data, code = UserModel.save(user)
        return Response(data, status=code, mimetype='application/json')

    def put(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        user = json_util.loads(json_util.dumps(request.json))
        data, code = UserModel.update(token, user)
        return Response(data, status=code, mimetype='application/json')
