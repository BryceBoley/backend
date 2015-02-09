from rest_framework import serializers
from models import *


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member


class EventSerializer(serializers.ModelSerializer):
    # members = MemberSerializer(many=True)

    class Meta:
        model = Event

        # def create(self, validated_data):
        # 	members_data = validated_data.pop('members')
        # 	event = Event.objects.create(**validated_data)
        # 	for member in members_data:
        # 		try:
        # 			member = Members.objects.get(name=member["member"])
        # 		except Members.DoesNotExist:
        # 			member = Members.objects.create(**member)
        # 		event.members.add(member)
        #
        # 	return event