from django.conf.urls import url
from . import views
from Src.web.Apis import SignupUser
from Src.web.Apis import LoginUser
from Src.web.Apis.Cart import Cart
from Src.web.Apis.Product import Product

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^SignupUser/$', SignupUser.sign_up_user, name='SignupUser'),
    url(r'^LoginUser/$', LoginUser.login_user, name='LoginUser'),
    url(r'^AddProduct/$', Product().add_product, name='AddProduct'),
    url(r'^GetProducts/$', Product().get_products, name='GetProducts'),
    url(r'^Cart/AddItem/$', Cart().add_item, name='AddItem'),
    url(r'^Cart/GetItems/$', Cart().get_items, name='GetItem'),
    url(r'^Cart/RemoveItem/$', Cart().remove_item, name='RemoveItem'),

]

