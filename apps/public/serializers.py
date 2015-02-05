from rest_framework import serializers
from models import *


class DinnerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Dinner