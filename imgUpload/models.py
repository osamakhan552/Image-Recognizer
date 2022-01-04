from django.db import models

class upload(models.Model):
    img = models.ImageField(upload_to='images/',blank=True) 
