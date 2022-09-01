from bson import json_util
from flask_restful import Resource
from flask import request, Response
from Services.ProductService import ProductService


class ProductsController(Resource):
    def get(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        data, code = ProductService.getAll(token)
        return Response(data, status=code, mimetype='application/json')
