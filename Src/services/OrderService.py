from Src.repository.OrderRepository import OrderRepository
from Src.repository.CartRepository import CartRepository
from Src.Domain.models.CartDomainModel import CartDomainModel
from Src.Domain.models.OrderDomainModel import OrderDomainModel
from Src.services.Manager.AuthorizationManager import extract_user_id
from django.core.handlers.wsgi import WSGIRequest
import datetime


class OrderService:
    repository_order: OrderRepository
    repository_cart: CartRepository

    def __init__(self, repository_order: OrderRepository, repository_cart: CartRepository):

        self.repository_order = repository_order
        self.repository_cart = repository_cart

    def checkout(self, request: WSGIRequest):
        # get user_id from token
        user_id = extract_user_id(request)

        item = self.repository_cart.find_record_by_user_id(user_id)
        cart_id = item.cart_id

        creation_date = datetime.datetime.now()

        model = OrderDomainModel(user_id, cart_id, creation_date)
        self.repository_order.insert(model)

        # update order_status of cart
        self.repository_cart.update_record_by_cart_id(cart_id)

        # create new cart for user
        model_cart = CartDomainModel(user_id, -1, creation_date)
        self.repository_cart.insert(model_cart)

        return True


