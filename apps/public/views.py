from rest_framework import generics
from serializers import *


class EventList(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class AddEvent(generics.CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EditEvent(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class AddMember(generics.CreateAPIView):
    serializer_class = MemberSerializer
    queryset = Members.objects.all()


class MembersList(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()    queryset = Event.objects.all()


class UserProfile(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = UserProfile.objects.all()