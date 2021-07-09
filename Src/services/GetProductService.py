from Src.repository.ProductRepository import ProductRepository
from Src.Domain.models.ProductDomainModel import ProductDomainModel


class GetProductService:
    repository: ProductRepository

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_products(self):
        products = self.repository.get_all()
        list_product = ProductDomainModel.asJSON(products)

        return list_product
