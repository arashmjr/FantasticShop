from Src.repository.OrderRepository import OrderRepository
from Src.repository.CartRepository import CartRepository
from Src.repository.CartProductRepository import CartProductRepository
from Src.repository.ProductRepository import ProductRepository
from Src.Domain.models.CartDomainModel import CartDomainModel
from Src.Domain.models.OrderDomainModel import OrderDomainModel
from Src.services.Manager.AuthorizationManager import extract_user_id
from django.core.handlers.wsgi import WSGIRequest
import datetime


class OrderService:
    repository_order: OrderRepository
    repository_cart: CartRepository
    repository_cart_product: CartProductRepository
    repository_product: ProductRepository

    def __init__(self, repository_order: OrderRepository, repository_cart: CartRepository,
                 repository_cart_product: CartProductRepository, repository_product: ProductRepository):

        self.repository_order = repository_order
        self.repository_cart = repository_cart
        self.repository_cart_product = repository_cart_product
        self.repository_product = repository_product

    def checkout(self, request: WSGIRequest):
        # get user_id from token
        user_id = extract_user_id(request)

        item = self.repository_cart.find_record_by_user_id(user_id)
        cart_id = item.cart_id
        print(cart_id)

        creation_date = datetime.datetime.now()

        model = OrderDomainModel(user_id, cart_id, creation_date)
        self.repository_order.insert(model)

        # update order_status of cart
        self.repository_cart.checkout_by_cart_id(cart_id)

        # create new cart for user
        model_cart = CartDomainModel(user_id, -1, creation_date)
        self.repository_cart.insert(model_cart)

        # get product_id's of cart
        list_products = self.repository_cart_product.find_records_by_cart_id(cart_id)
        list_product_ids = []
        for item in list_products:
            product_id = item.product_id.product_id
            list_product_ids.append(product_id)

        # update quantity of product in product table
        for item in list_product_ids:
            self.repository_product.update_quantity_by_product_id(item)

        return True


