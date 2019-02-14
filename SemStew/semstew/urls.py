from django.urls import path
from . import views

app_name = 'semstew'

urlpatterns = [
    path('', views.index, name='index'),
    path('branches/<int:language_id>', views.branches, name='branches'),
    path('offer/<int:language_id>', views.offer, name='offer'),
    path('delivery/<int:language_id>', views.delivery, name='delivery'),
    path('reservation/<int:language_id>', views.reservation, name='reservation'),
    path('aboutus/<int:language_id>', views.about_us, name='about_us'),
    path('contact/<int:language_id>', views.contact, name='contact'),
]
