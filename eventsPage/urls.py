from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'eventsPage'

urlpatterns = [
    path( '', views.event_list ),
]