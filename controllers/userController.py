
from bson import json_util
from flask_restful import Resource
from flask import request, Response
from Services.UserService import UserService


class UserController(Resource):
    def get(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        data, code = UserService.find(token)
        return Response(data, status=code, mimetype='application/json')

    def post(self):
        user = json_util.loads(json_util.dumps(request.json))
        data, code = UserService.save(user)
        return Response(data, status=code, mimetype='application/json')

    def put(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        user = json_util.loads(json_util.dumps(request.json))
        data, code = UserService.update(token, user)
        return Response(data, status=code, mimetype='application/json')
