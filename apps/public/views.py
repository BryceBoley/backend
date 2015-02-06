from django.shortcuts import render
from rest_framework import generics
from serializers import *
# Create your views here.


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class UserProfile(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = UserProfile.objects.all()