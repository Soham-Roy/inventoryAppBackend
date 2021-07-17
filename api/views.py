from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from eventsPage.models import Event
from inventoryPage.models import Inventory
from api.serializers import EventSerializer, InventorySerializer

# Create your views here.
@api_view(['GET'])
def event_list(request):
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    if request.method == "GET":
        serializer = EventSerializer(events, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)     

@api_view(['PUT'])
def update_event(request):
    try:
        event = Event.objects.get()
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = EventSerializer(event, data= event.eventName)
        data = {}
        if ( serializer.is_valid ):
            serializer.save()
            data["operation"] = "update successful"
            return Response(data= data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_event(request):
    try:
        event = Event.objects.get()
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = event.delete()
        data = {}
        if operation:
            data["operation"] = "delete successful"
        else:
            data["operation"] = "delete failed"    
        return Response(data= data) 

@api_view(['POST'])
def create_event(request):
    event = Event()
    if request.method == "PUT":
        serializer = EventSerializer(event, data= event.eventName)
        data = {}
        if ( serializer.is_valid ):
            serializer.save()
            data["operation"] = "update successful"
            return Response(data= data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def inventory_list(request):
    try:
        inventories = Inventory.objects.all()
    except Inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    if request.method == "GET":
        serializer = InventorySerializer(inventories, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)        