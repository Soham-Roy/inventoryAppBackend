from eventsPage.models import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 
            'eventName', 
            'organiser', 
            'start', 
            'end',
            'venue', 
            'contact', 
            'postCreationTime'
        ]

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 
            'inventoryName', 
            'ownerClub', 
            'available', 
            'quantityTotal',
            'lastUpdated'
        ]        