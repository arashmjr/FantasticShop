from django.conf.urls import url
from . import views
from Src.web.Apis import SignupUser
from Src.web.Apis import LoginUser

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^SignupUser/$', SignupUser.sign_up_user, name='SignupUser'),
    url(r'^LoginUser/$', LoginUser.login_user, name='LoginUser'),

]

