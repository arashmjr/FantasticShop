from Src.repository.ProductRepository import ProductRepository
from Src.Domain.models.ProductDomainModel import ProductDomainModel


class ProductService:
    repository: ProductRepository

    def __init__(self, repository: ProductRepository):

        self.repository = repository

    def add_product(self, json: str):

        model = ProductDomainModel(json['product_id'], json['category_id'],
                                   json['name'], json['thumbnail'], json['price'], json['quantity'])

        self.repository.insert(model)
        return True

    def get_products(self):
        products = self.repository.get_all()
        list_product = ProductDomainModel.asJSON(products)

        return list_product
