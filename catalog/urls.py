
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import base, contacts, products, home

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', products, name='products'),
    path('base/', base, name='base')
]
