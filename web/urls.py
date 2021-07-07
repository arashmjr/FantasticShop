from django.conf.urls import url
from . import views
# from Src.web.Apis.SaveUser import SaveUser
from Src.web.Apis import SignupUser

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^SignupUser/$', SignupUser.sign_up_user, name='SignupUser'),

]
