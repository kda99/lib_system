from django.db import models

class Organization(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)