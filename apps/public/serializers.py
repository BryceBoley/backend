__author__ = 'macuser'
from rest_framework import serializers
from models import *



class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event






    def get_events(self, obj):
        events = Events.objects.filter(event=obj.id)
        serializer = EventSerializer(events, many=True)
        return serializer.data


