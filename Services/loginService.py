
from bson import json_util
from flask_restful import Resource
from models.LoginModel import LoginModel
from flask import request, Response


class LoginService(Resource):
    def post(self):
        user = json_util.loads(json_util.dumps(request.json))
        data, code = LoginModel.login(user)
        return Response(data, status=code, mimetype='application/json')
