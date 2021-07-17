from django.conf.urls import url
from . import views
from Src.web.Apis import SignupUser
from Src.web.Apis import LoginUser
from Src.web.Apis.Cart import Cart
from Src.web.Apis.Product import Product
from Src.services.Manager.AuthorizationManager import login_required

urlpatterns = [
    url(r'^SignupUser/$', SignupUser.sign_up_user),
    url(r'^LoginUser/$', LoginUser.login_user),
    url(r'^AddProduct/$', Product().add_product),
    url(r'^GetProducts/$', Product().get_products),
    url(r'^Cart/AddItem/$', Cart().add_item),
    url(r'^Cart/GetItems/$', Cart().get_items),
    url(r'^Cart/RemoveItem/$', Cart().remove_item),

]

