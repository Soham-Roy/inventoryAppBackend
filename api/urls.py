from django.urls import path
from api.views import event_list

app_name = 'eventsPage'

urlpatterns = [
    path('events/', event_list, name='events'),
]