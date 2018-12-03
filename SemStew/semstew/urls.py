from django.conf.urls import url
from . import views

urlpatterns = [
    #Customer's home page

    url(r'^$', views.index, name='index'),
]
