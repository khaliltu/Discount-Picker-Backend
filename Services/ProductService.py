

from Services.UserService import UserService
from Services.userHistoryService import UserHistoryService
from models.ProductModel import ProductModel
from bson.json_util import dumps
from models.utils.ProductUtils import registerProductDetails


class ProductService():
    def getOne(token, id):
        data, code = UserService.find(token, cleanObjects=False)
        if (code == 200):
            product = ProductModel.getOne(id)
            registerProductDetails(product)
            userHistory = UserHistoryService.find(data['email'])
            l = list(userHistory)
            if(not l):
                UserHistoryService.add(product, data['email'])
            else:
                UserHistoryService.update(product, data["email"])
            data = dumps(product)
        return data, code

    def getSome(number):
        return ProductModel.getSome(number)

    def getAll(token):
        data, code = UserService.find(token, cleanObjects=False)
        if (code == 200):
            products = ProductModel.getAll()
            recommandedProducts = UserHistoryService.getRecommandations(
                data["email"], products)
            data = {"products": products,
                    "recommandedProducts": recommandedProducts}
            data = dumps(data)
        return data, code

    def deleteAll():
        ProductModel.deleteAll()
