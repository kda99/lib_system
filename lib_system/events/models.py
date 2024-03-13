from django.db import models
from organizations.models import Organization

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(upload_to='event_images/')
    date = models.DateField()