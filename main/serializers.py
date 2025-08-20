from rest_framework import serializers
from .models import Starter

class StarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starter
        fields = "__all__"