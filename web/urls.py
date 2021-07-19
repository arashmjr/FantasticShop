from django.conf.urls import url
from . import views
from Src.web.apis import SignupUser
from Src.web.apis import LoginUser
from Src.web.apis import AdminAuth
from Src.web.apis.Cart import Cart
from Src.web.apis.Product import Product
from Src.web.apis.Order import Order

urlpatterns = [
    url(r'^SignupUser/$', SignupUser.sign_up_user),
    url(r'^LoginUser/$', LoginUser.login_user),
    url(r'^SignupAdmin/$', AdminAuth.sign_up_admin),
    url(r'^LoginAdmin/$', AdminAuth.login_admin),
    url(r'^AddProduct/$', Product().add_product),
    url(r'^GetProducts/$', Product().get_products),
    url(r'^Cart/AddItem/$', Cart().add_item),
    url(r'^Cart/GetItems/$', Cart().get_items),
    url(r'^Cart/RemoveItem/$', Cart().remove_item),
    url(r'^checkout/$', Order().checkout),

]


