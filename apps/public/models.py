from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Event(models.Model):
	host = models.CharField(max_length=50)
	location = models.TextField(help_text="Where should members go for your dinner group?")
	when = models.TextField(blank=True, help_text="When event is to take place")
	description = models.TextField(blank=True, help_text="Describe your group")
	members = models.TextField(blank=True)
	comments = models.TextField(blank=True)
	#pics = models.ImageField(upload_to='photos', blank=True, null=True)

	def __str__(self):
		return self.host


class Member(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


# class UserProfile(models.Model):
# # user = models.OneToOneField(User)
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
