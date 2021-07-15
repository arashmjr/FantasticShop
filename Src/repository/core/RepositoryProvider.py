from Src.repository.SaveUserRepository import SaveUserRepository
from Src.repository.ProductRepository import ProductRepository
from Src.repository.CartRepository import CartRepository
from Src.repository.CartProductRepository import CartProductRepository
from Src.repository.core.CoreDatabase import CoreDatabase
from Src.Domain.Entities import User, Product, Carts, CartProducts


class RepositoryProvider:
    database = CoreDatabase.get_instance()

    def make_user_profile(self):
        collection = User
        return SaveUserRepository(collection)

    def make_products(self):
        collection = Product
        return ProductRepository(collection)

    def make_Cart(self):
        collection = Carts
        return CartRepository(collection)

    def make_cart_product(self):
        collection = CartProducts
        return CartProductRepository(collection)

    # def make_packages(self):
    #     collection = self.database.user_db["packages"]
    #     return PackagesRepository(collection)
