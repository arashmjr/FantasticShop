import datetime


class CartDomainModel:
    # Cart_id: int
    user_id: int
    product_id: int
    product_name: str
    quantity: int
    isActive: bool
    creation_date: datetime

    def __init__(self, user_id: int, product_id: int, product_name: str,
                 quantity: int, isActive: bool, creation_date: datetime):

        # self.Cart_id = Cart_id
        self.user_id = user_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.isActive = isActive
        self.creation_date = creation_date

    def to_dict(self):
        return {

                "user_id": self.user_id,
                "product_id": self.product_id,
                "product_name": self.product_name,
                "quantity": self.quantity,
                "isActive": self.isActive,
                "creation_date": self.creation_date
                }

    @staticmethod
    def asJSON(products):
        list_products = []
        for item in products:
            result = {
                'Cart_id': item.Cart_id,
                'user_id': item.user_id,
                'product_id': item.product_id,
                'product_name': item.product_name,
                'quantity': item.quantity,
                'isActive': item.isActive,
                'creation_date': item.creation_date
            }
            list_products.append(result)
        return list_products


