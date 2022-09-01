
from bson import json_util
from flask_restful import Resource
from flask import request, Response

from Services.loginService import LoginService


class LoginController(Resource):
    def post(self):
        user = json_util.loads(json_util.dumps(request.json))
        data, code = LoginService.login(user)
        return Response(data, status=code, mimetype='application/json')

    def put(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        user = json_util.loads(json_util.dumps(request.json))
        data, code = LoginService.update(token, user)
        return Response(data, status=code, mimetype='application/json')
