from django.db import models

class addText(models.Model):
    text = models.CharField(max_length=100)
    position = models.CharField(max_length=2, default='bc')
