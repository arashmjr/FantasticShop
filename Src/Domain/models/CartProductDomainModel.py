import datetime
from Src.Domain.Entities import User,Carts,Product

class CartProductDomainModel:

    product_id: int
    cart_id: int
    user_id: int
    creation_date: datetime
    quantity: int
    order_status: int

    def __init__(self, product_id: int, cart_id: int, user_id: int, creation_date: datetime,
                 quantity: int, order_status: int):

        self.product_id = product_id
        self.cart_id = cart_id
        self.user_id = user_id
        self.creation_date = creation_date
        self.quantity = quantity
        self.order_status = order_status

    def to_dict(self):
        return {
                "product_id": Product(self.product_id),
                "cart_id": Carts(self.cart_id),
                "user_id": User(self.user_id),
                "creation_date": self.creation_date,
                "quantity": self.quantity,
                "order_status": self.order_status
                }
