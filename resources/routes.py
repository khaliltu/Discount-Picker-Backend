
from Services.productsService import ProductsService
from Services.productService import ProductService
from Services.userService import UserService
from Services.loginService import LoginService
from Services.homeProductsService import HomeProductService


def initialize_routes(api):
    api.add_resource(UserService, "/api/v1/user")
    api.add_resource(LoginService, "/api/v1/login")
    api.add_resource(ProductsService, "/api/v1/products")
    api.add_resource(ProductService, "/api/v1/product")
    api.add_resource(HomeProductService, "/api/v1/home-product")
