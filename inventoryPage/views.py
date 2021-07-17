from django.shortcuts import render
from django.http import HttpResponse
from inventoryPage.models import Inventory

# Create your views here.
def inventory_list(request):
    inventories = Inventory.objects.all().order_by('date')
    return HttpResponse(inventories)