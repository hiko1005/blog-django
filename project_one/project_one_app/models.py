from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=True)
    text = models.CharField(max_length=255, null=False, blank=True)