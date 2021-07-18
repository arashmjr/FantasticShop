from Src.Domain.Entities import User, Carts, Order
import datetime


class OrderDomainModel:

    user_id: int
    cart_id: int
    creation_date: datetime

    def __init__(self, user_id: int, cart_id: int, creation_date: datetime):

        self.user_id = user_id
        self.cart_id = cart_id
        self.creation_date = creation_date

    def to_dict(self):
        return {
                "user_id": User(self.user_id),
                "cart_id": Carts(self.cart_id),
                "creation_date": self.creation_date

                }

