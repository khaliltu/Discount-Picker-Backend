
from Services.userService import UserService


def initialize_routes(api):
    api.add_resource(UserService, "/api/v1/user")
