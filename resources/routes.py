
from controllers.productsController import ProductsService
from controllers.productController import ProductService
from controllers.userController import UserService
from controllers.loginController import LoginService
from controllers.homeProductsController import HomeProductService


def initialize_routes(api):
    api.add_resource(UserService, "/api/v1/user")
    api.add_resource(LoginService, "/api/v1/login")
    api.add_resource(ProductsService, "/api/v1/products")
    api.add_resource(ProductService, "/api/v1/product")
    api.add_resource(HomeProductService, "/api/v1/home-product")
