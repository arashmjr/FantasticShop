import datetime


class ShoppingCartDomainModel:
    shoppingCart_id: int
    user_id: int
    product_id: int
    product_name: str
    quantity: int
    isActive: bool
    creation_date: datetime

    def __init__(self, shoppingCart_id: int, user_id: int, product_id: int, product_name: str,
                 quantity: int, isActive: bool, creation_date: datetime):

        self.shoppingCart_id = shoppingCart_id
        self.user_id = user_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.isActive = isActive
        self.creation_date = creation_date

    def to_dict(self):
        return {"shoppingCart_id": self.shoppingCart_id,
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
                'shoppingCart_id': item.shoppingCart_id,
                'user_id': item.user_id,
                'product_id': item.product_id,
                'product_name': item.product_name,
                'quantity': item.quantity,
                'isActive': item.isActive,
                'creation_date': item.creation_date
            }
            list_products.append(result)
        return list_products


