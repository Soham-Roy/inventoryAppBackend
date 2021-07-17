from django.db import models

# Create your models here.
class Inventory(models.Model):
    inventoryName = models.CharField(max_length=80)
    ownerClub = models.CharField(max_length=80)
    available = models.IntegerField()
    quantityTotal = models.IntegerField()
    lastUpdated = models.IntegerField()
    
    def __str__(self):
        return self.inventoryName