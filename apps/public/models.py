from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Event(models.Model):
    host = models.ForeignKey(User)
    description = models.TextField(blank=True, help_text="Describe your group")
    location = models.TextField(help_text="Where should members go for your dinner group?")
    # attendees = models.ForeignKey(Groups)
    food_allergies = models.TextField(blank=True)
    pics = models.ImageField(upload_to='photos', blank=True, null=True)
    # creator = models.OneToOneField(User)
    # date = models.parse_datetime()

    def __str__(self):
        return self.name


class Members(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


# class UserProfile(models.Model):
#     # user = models.OneToOneField(User)
#     phone_number = models.CharField(max_length=15)
#     street = models.CharField(max_length=75, blank=False)
#     city = models.CharField(max_length=50, blank=False)
#     state = models.CharField(max_length=35, blank=False)
#     food_allergies = models.TextField(max_length=75,
#                                       default="Have any food allergies you want the group to know about?", blank=True)
#     profile_picture = models.ImageField(upload_to='photos', blank=True, null=True)
#
#     def __str__(self):
#         return self.user.names


# class Group(models.Model):
# name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True, help_text="Describe your group")
#     pics = models.ImageField(upload_to='photos', blank=True, null=True)
#     event = models.ManyToManyField(Event)
#     blah = models.TextField()
#
#     def __str__(self):
#         return self.user.name