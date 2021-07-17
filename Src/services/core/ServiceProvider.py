from Src.repository.core.RepositoryProvider import RepositoryProvider
from Src.services.Manager.AuthorizationManager import login_required
from Src.services.SignupUserService import SignupUserService
from Src.services.LoginUserService import LoginUserService
from Src.services.ProductService import ProductService
from Src.services.CartService import CartService


class ServiceProvider:
    repository_provider: RepositoryProvider

    def __init__(self):
        self.repository_provider = RepositoryProvider()

    def make_signup_user_service(self):
        return SignupUserService(self.repository_provider.make_user_profile(),
                                 self.repository_provider.make_Cart())

    def make_login_user_service(self):
        return LoginUserService(self.repository_provider.make_user_profile())

    def make_product_service(self):
        return ProductService(self.repository_provider.make_products())

    def make_cart_service(self):
        return CartService(self.repository_provider.make_Cart(),
                           self.repository_provider.make_products(),
                           self.repository_provider.make_cart_product())





