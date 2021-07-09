from Src.repository.SaveUserRepository import SaveUserRepository
from Src.repository.ProductRepository import ProductRepository
from Src.repository.core.CoreDatabase import CoreDatabase
from Src.Domain.Entities import User, Product


class RepositoryProvider:
    database = CoreDatabase.get_instance()

    def make_user_profile(self):
        collection = User
        return SaveUserRepository(collection)

    def make_products(self):
        collection = Product
        return ProductRepository(collection)

    # def submit_orders(self):
    #     collection = self.database.user_db["orders"]
    #     return SaveOrderRepository(collection)
    #
    # def make_user_follows(self):
    #     collection = self.database.user_db["userFollow"]
    #     return UserFollowRepository(collection)
    #
    # def make_packages(self):
    #     collection = self.database.user_db["packages"]
    #     return PackagesRepository(collection)
