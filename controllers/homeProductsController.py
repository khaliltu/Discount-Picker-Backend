from bson import json_util
from flask_restful import Resource
from flask import request, Response
from models.ProductModel import ProductModel


class HomeProductService (Resource):
    def get(self):
        number = json_util.loads(
            json_util.dumps(request.headers.get('number')))
        data, code = ProductModel.getSome(int(number))
        return Response(data, status=code, mimetype='application/json')
