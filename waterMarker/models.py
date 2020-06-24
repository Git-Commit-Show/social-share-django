from django.db import models

# Create your models here.
class Images(models.Model):
    text=models.CharField(blank=True, max_length=100)
    position=models.CharField(max_length=3,default='bcl')
    logo= models.ImageField(upload_to='images/Uploads')
    path=models.CharField(blank=True, max_length=100)
