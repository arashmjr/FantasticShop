from Src.repository.CartRepository import CartRepository
from Src.repository.ProductRepository import ProductRepository
from Src.Domain.models.CartDomainModel import CartDomainModel
import datetime


class CartService:
    repository_cart: CartRepository
    repository_product: ProductRepository

    def __init__(self, repository_cart: CartRepository, repository_product: ProductRepository):

        self.repository_cart = repository_cart
        self.repository_product = repository_product

    def add_item(self, json: str):

        creation_date = datetime.datetime.now()
        model = CartDomainModel(json['user_id'],
                                json['product_id'], json['product_name'], json['quantity'],
                                json['isActive'], creation_date)

        self.repository_cart.insert(model)
        self.repository_product.update_record_by_product_id(model.product_id)

        # item = self.repository_product.find_record_by_product_id(model.product_id)
        # print(item.quantity)

        return True

    def get_items(self):
        products = self.repository_cart.get_all()
        list_product = CartDomainModel.asJSON(products)
        return list_product

    def remove_item(self, json):
        self.repository_cart.remove_record(json['shoppingCart_id'])
        return True




