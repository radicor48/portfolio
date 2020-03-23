from django.db import models
from datetime import datetime
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=50, blank=True)
    pub_date = models.DateTimeField()
    body = models.TextField(blank = True)
    image = models.ImageField(upload_to='images/')
