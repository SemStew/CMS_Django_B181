from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'semstew'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^branches/', views.branches, name='branches'),
    url(r'^offer/', views.offer, name='offer'),
    url(r'^delivery/', views.delivery, name='delivery'),
    url(r'^reservation/', views.reservation, name='reservation'),
    path('aboutus/<int:language_id>', views.about_us, name='about_us'),
    url(r'^contact/', views.contact, name='contact'),
]
