
class ProductDomainModel:
    product_id: int
    category_id: int
    name: str
    thumbnail: str
    price: int
    quantity: int

    def __init__(self, product_id: int, category_id: int, name: str, thumbnail: str
                 ,price: int, quantity: int):

        self.product_id = product_id
        self.category_id = category_id
        self.name = name
        self.thumbnail = thumbnail
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {"product_id": self.product_id,
                "category_id": self.category_id,
                "name": self.name,
                "thumbnail": self.thumbnail,
                "price": self.price,
                "quantity": self.quantity
                }

    @staticmethod
    def asJSON(products):
        list_products = []
        for item in products:
            result = {
                'product_id': item.product_id,
                'category_id': item.category_id,
                'name': item.name,
                'thumbnail': item.thumbnail,
                'price': item.price,
                'quantity': item.quantity
            }
            list_products.append(result)
        return list_products





