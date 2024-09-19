from django.db import models
from django.conf import settings

class Newbakes(models.Model):
    name =models.CharField(max_length=50)
    image =models.ImageField(upload_to="sorts")
    category = models.CharField(max_length=255)
    current_price = models.CharField(max_length=20,default=settings.DEFAULT_CURRENCY)
    size = models.CharField(max_length=20, blank=True, null=True)
    date_posted= models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    flavour= models.CharField(max_length=80)
    layers_display =models.TextField(blank=True, null=True)
    cakecategoryIdentifier =models.CharField(max_length=30) 
    
