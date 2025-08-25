from rest_framework import serializers
from apps.professions.models import Profession, ProfessionDetail

class ProfessionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionDetail
        fields = "__all__"

class ProfessionSerializer(serializers.ModelSerializer):
    details = ProfessionDetailSerializer(many=True, read_only=True, source="professiondetail_set")

    class Meta:
        model = Profession
        fields = "__all__"