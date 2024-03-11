from django.db import models
from organizations.models import Organization


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    organizations = models.ManyToManyField(Organization)

    def __str__(self):
        return self.name