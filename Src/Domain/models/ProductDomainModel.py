
class ProductDomainModel:

    category_id: int
    name: str
    thumbnail: str
    price: int
    usl_photo: str
    quantity: int

    def __init__(self, category_id: int, name: str, thumbnail: str
                 ,price: int, url_photo: int, quantity: int):

        self.category_id = category_id
        self.name = name
        self.thumbnail = thumbnail
        self.price = price
        self.url_photo = url_photo
        self.quantity = quantity

    def to_dict(self):
        return {
                "category_id": self.category_id,
                "name": self.name,
                "thumbnail": self.thumbnail,
                "price": self.price,
                "url_photo": self.url_photo,
                "quantity": self.quantity
                }

    @staticmethod
    def asJSON(products):
        list_products = []
        for item in products:
            result = {

                'category_id': item.category_id,
                'name': item.name,
                'thumbnail': item.thumbnail,
                'price': item.price,
                'url_photo': item.url_photo
            }
            list_products.append(result)
        return list_products





