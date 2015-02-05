from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Event(models.Model):
	name = models.CharField(max_length=100)
	event_host = models.CharField(max_length=100, null=True)
	location = models.TextField(help_text="where the event is being held")
	date = models.DateTimeField()
	description = models.TextField(blank=True, null=True, help_text="Describe your event")
	pics = models.ImageField(upload_to='photos', blank=True, null=True)
	messages = models.TextField(blank=True, null=True, help_text="attendees allergies")
	attendees = models.CharField(max_length=100, blank=True, null=True, help_text="Describe your group")

	def __str__(self):
		return self.name
