from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'inventoryPage'

urlpatterns = [
    path( '', views.inventory_list ),
]