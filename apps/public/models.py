from django.db import models
from datetime import datetime


class Event(models.Model):
    title = models.CharField(max_length=100)
    start = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now())
    comment = models.TextField(blank=True, null=True, help_text="comment")
    host = models.TextField(blank=True, null=True, help_text="Who is hosting")
    when = models.TextField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.title


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, default="", blank=True)
    street = models.CharField(max_length=75, default="")
    apartment_number = models.CharField(max_length=25, default="", blank=True)
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=35, default="")
    zip = models.CharField(max_length=20, default="")
    allergy = models.TextField(max_length=75, default="", blank=True)
    profile_picture = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
