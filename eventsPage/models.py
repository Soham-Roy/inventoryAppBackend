from django.db import models

# Create your models here.
class Event(models.Model):
    #ID, Event Name, start, end, venue, duration, contact details,
    eventName = models.CharField(max_length=80)
    organiser = models.CharField(max_length=80)
    start = models.DateTimeField(null = True)
    end = models.DateTimeField(null = True)
    venue = models.TextField()
    contact = models.TextField()
    postCreationTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.organiser

    def duration(self):
        return self.end - self.start

