from bson import json_util
from flask_restful import Resource
from flask import request, Response
from models.ProductModel import ProductModel


class ProductService (Resource):
    def get(self):
        token = json_util.loads(json_util.dumps(request.headers.get('token')))
        id = json_util.loads(json_util.dumps(request.headers.get('id')))
        data, code = ProductModel.getOne(token, id)
        return Response(data, status=code, mimetype='application/json')
