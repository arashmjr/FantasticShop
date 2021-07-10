from Src.repository.core.RepositoryProvider import RepositoryProvider
from Src.services.Manager.AuthorizationManager import AuthorizationManager
from Src.services.SignupUserService import SignupUserService
from Src.services.LoginUserService import LoginUserService
from Src.services.AddProductServise import AddProductService
from Src.services.GetProductService import GetProductService
from Src.services.ShoppingCartService import ShoppingCartService


class ServiceProvider:
    repository_provider: RepositoryProvider
    auth: AuthorizationManager

    def __init__(self):
        self.repository_provider = RepositoryProvider()
        self.auth = AuthorizationManager()

    def make_signup_user_service(self):
        return SignupUserService(self.repository_provider.make_user_profile(),  self.auth)

    def make_login_user_service(self):
        return LoginUserService(self.repository_provider.make_user_profile(), self.auth)

    def make_add_product_service(self):
        return AddProductService(self.repository_provider.make_products())

    def make_get_products_service(self):
        return GetProductService(self.repository_provider.make_products())

    def make_shopping_cart_service(self):
        return ShoppingCartService(self.repository_provider.make_shoppingCart())




