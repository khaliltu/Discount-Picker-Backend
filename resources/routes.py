
from Services.userService import UserService
from Services.loginService import LoginService


def initialize_routes(api):
    api.add_resource(UserService, "/api/v1/user")
    api.add_resource(LoginService, "/api/v1/login")
