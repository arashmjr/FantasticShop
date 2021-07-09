from django.conf.urls import url
from . import views
from Src.web.Apis import SignupUser
from Src.web.Apis import LoginUser
from Src.web.Apis import AddProduct, GetProducts

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^SignupUser/$', SignupUser.sign_up_user, name='SignupUser'),
    url(r'^LoginUser/$', LoginUser.login_user, name='LoginUser'),
    url(r'^AddProduct/$', AddProduct.add_product, name='AddProduct'),
    url(r'^GetProducts/$', GetProducts.get_products, name='GetProducts'),

]

