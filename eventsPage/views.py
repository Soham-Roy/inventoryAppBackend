from django.shortcuts import render
from .models import Event
from django.http import HttpResponse

# Create your views here.
def event_list(request):
    events = Event.objects.all().order_by('date')
    return HttpResponse(events)