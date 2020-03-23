from django.db import models
from datetime import datetime
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=50, blank=True)
    pub_date = models.DateTimeField()
    body = models.TextField(blank = True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
    
    
    def summary(self):
        return self.body[:50]
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %e, %Y')