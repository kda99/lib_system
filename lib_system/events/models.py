from django.db import models
from organizations.models import Organization


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(upload_to='events', blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name