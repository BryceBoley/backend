from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, help_text="Describe your group")
    location = models.TextField(help_text="What can people put into maps to get to your house")
    # members = models.ManyToManyField(User)
    food_allergies = models.TextField(blank=True, null=True)
    pics = models.ImageField(upload_to='photos', blank=True, null=True)
    # creator = models.OneToOneField(User)
    # date = models.parse_datetime()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    # user = models.ForeignKey(User)
    phone_number = models.CharField(max_length=15)
    street = models.CharField(max_length=75, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=35, blank=True)
    food_allergies = models.TextField(max_length=75, default="Any food allergies?")
    profile_picture = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return u"%s" % self.user  # Need to change to user (according to model)


# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True, help_text="Describe your group")
#     pics = models.ImageField(upload_to='photos', blank=True, null=True)
#     event = models.ManyToManyField(Event)
#
#     def __str__(self):
#         return self.name