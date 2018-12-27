from django.conf.urls import url
from . import views

app_name = 'semstew'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^branches/', views.branches, name='branches'),
    url(r'^offer/', views.offer, name='offer'),
    url(r'^delivery/', views.delivery, name='delivery'),
    url(r'^reservation/', views.reservation, name='reservation'),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^contact/', views.contact, name='contact'),
]
