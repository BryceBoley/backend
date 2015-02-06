from django.db import models


class Event(models.Model):
	name = models.CharField(max_length=50)
	event_host = models.CharField(max_length=100, null=True)
	location = models.TextField(help_text="where the event is being held")
	when = models.TextField(max_length=100)
	description = models.TextField(blank=True, null=True, help_text="Describe your event")
	# pics = models.ImageField(upload_to='photos', blank=True, null=True)
	messages = models.TextField(blank=True, null=True, help_text="Messages about event")
	members = models.CharField(max_length=250, null=True)

	def __str__(self):
		return self.name


class Members(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name
