from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from eventsPage.models import Event
from api.serializers import EventSerializer

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