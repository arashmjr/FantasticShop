from Src.repository.ShoppingCartRepository import ShoppingCartRepository
from Src.Domain.models.ShoppingCartDomainModel import ShoppingCartDomainModel
import datetime


class ShoppingCartService:
    repository: ShoppingCartRepository

    def __init__(self, repository: ShoppingCartRepository):

        self.repository = repository

    def add_item(self, json: str):

        creation_date = datetime.datetime.now()
        model = ShoppingCartDomainModel(json['shoppingCart_id'], json['user_id'],
                                   json['product_id'], json['product_name'], json['quantity'],
                                   json['isActive'], creation_date)

        self.repository.insert(model)
        return True

    def get_items(self):
        products = self.repository.get_all()
        list_product = ShoppingCartDomainModel.asJSON(products)
        return list_product

    def remove_item(self, json):
        self.repository.remove_record(json['shoppingCart_id'])
        return True




