from rest_framework import serializers
from models import *


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event