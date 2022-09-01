
from controllers.productsController import ProductsController
from controllers.productController import ProductController
from controllers.loginController import LoginController
from controllers.homeProductsController import HomeProductService
from controllers.userController import UserController


def initialize_routes(api):
    api.add_resource(UserController, "/api/v1/user")
    api.add_resource(LoginController, "/api/v1/login")
    api.add_resource(ProductsController, "/api/v1/products")
    api.add_resource(ProductController, "/api/v1/product")
    api.add_resource(HomeProductService, "/api/v1/home-product")
