from django.urls import path
from api.views import (
    event_list,
    inventory_list,
)

urlpatterns = [
    path('events/', event_list, name='events'),
    path('inventories/', inventory_list, name='inventories')
]