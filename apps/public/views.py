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
    queryset = Member.objects.all()


class MemberList(generics.ListAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class EditMember(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()