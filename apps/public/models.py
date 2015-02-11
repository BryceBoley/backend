from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Member(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, default="N/A")
    street = models.CharField(max_length=75, default="N/A")
    city = models.CharField(max_length=50, default="N/A")
    state = models.CharField(max_length=35, default="N/A")
    food_allergies = models.TextField(max_length=75, default="Have any food allergies?", blank=True)
    # profile_picture = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    when = models.TextField(help_text="When event is to take place")
    location = models.TextField(blank=True, help_text="Where should members go for your dinner group?")
    description = models.TextField(blank=True, help_text="Describe your group")
    comments = models.TextField(blank=True)
    #pics = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.when
