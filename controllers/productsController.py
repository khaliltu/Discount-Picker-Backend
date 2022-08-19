from bson import json_util
from flask_restful import Resource
from flask import request, Response

from models.ProductModel import ProductModel


class ProductsService(Resource):
    def get(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        data, code = ProductModel.getAll(token)
        return Response(data, status=code, mimetype='application/json')
