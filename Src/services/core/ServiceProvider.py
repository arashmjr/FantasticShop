from Src.repository.core.RepositoryProvider import RepositoryProvider
from Src.services.auth.SignupUserService import SignupUserService
from Src.services.auth.LoginUserService import LoginUserService
from Src.services.ProductService import ProductService
from Src.services.CartService import CartService
from Src.services.OrderService import OrderService
from Src.services.auth.AuthAdminService import AuthAdminService


class ServiceProvider:
    repository_provider: RepositoryProvider

    def __init__(self):
        self.repository_provider = RepositoryProvider()

    def make_signup_user_service(self):
        return SignupUserService(self.repository_provider.make_user_profile(),
                                 self.repository_provider.make_Cart())

    def make_signup_admin_service(self):
        return AuthAdminService(self.repository_provider.make_admin_profile(),
                                self.repository_provider.make_Cart())

    def make_login_user_service(self):
        return LoginUserService(self.repository_provider.make_user_profile())

    def make_login_admin_service(self):
        return AuthAdminService(self.repository_provider.make_admin_profile(),
                                self.repository_provider.make_Cart())

    def make_product_service(self):
        return ProductService(self.repository_provider.make_products())

    def make_cart_service(self):
        return CartService(self.repository_provider.make_Cart(),
                           self.repository_provider.make_products(),
                           self.repository_provider.make_cart_product())

    def make_order_service(self):
        return OrderService(self.repository_provider.submit_order(), self.repository_provider.make_Cart(),
                            self.repository_provider.make_cart_product(),
                            self.repository_provider.make_products())






