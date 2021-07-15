import datetime
from Src.Domain.Entities.User import User


class CartDomainModel:

    user_id: int
    order_status: int
    creation_date: datetime

    def __init__(self, user_id: int, order_status: int, creation_date: datetime):

        self.user_id = user_id
        self.order_status = order_status
        self.creation_date = creation_date

    def to_dict(self):
        return {

                "user_id": User(self.user_id),
                "order_status": self.order_status,
                "creation_date": self.creation_date
                }

    @staticmethod
    def asJSON(products):
        list_products = []
        for item in products:
            result = {
                'cart_id': item.cart_id,
                'user_id': item.user_id.user_id,
                'order_status': item.order_status,
                'creation_date': item.creation_date
            }
            list_products.append(result)
        return list_products


