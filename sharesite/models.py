from django.db import models

# Create your models here.
class PostData(models.Model):
	text=models.TextField()
	hashTags=models.TextField(blank=True)
	url=models.TextField(blank=True)


