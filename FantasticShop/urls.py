from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('web.urls')),
]
