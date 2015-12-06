from django.db import models
from django.utils import timezone
# Create your models here.
class Organization(models.Model):
    """docstring for Organization"""
    title = models.CharField(max_length=200)
    locations = models.TextField()
    category = models.CharField(max_length=200)
    mission_statement = models.TextField()
    def __str__(self):
        return self.title
class Event(models.Model):
    """docstring for Event"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(
            default=timezone.now)
    end_date = models.DateTimeField(
            blank=True, null=True)
    organization = models.ForeignKey(Organization,null=True,blank=True)
    def __str__(self):
        return self.title
from django.contrib import admin
admin.site.register(Event)


admin.site.register(Organization)
