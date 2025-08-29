from rest_framework import serializers
from .models import Resume, PersonalInfo, Education, Language, WorkExperience, Career

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = "__all__"
        extra_kwargs = {"resume": {"read_only": True}}

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        extra_kwargs = {"resume": {"read_only": True}}

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"
        extra_kwargs = {"resume": {"read_only": True}}

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"
        extra_kwargs = {"resume": {"read_only": True}}

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = "__all__"
        extra_kwargs = {"resume": {"read_only": True}}

class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    personal_info = PersonalInfoSerializer(required=False, allow_null=True)
    education = EducationSerializer(many=True, required=False)
    languages = LanguageSerializer(many=True, required=False)
    experiences = WorkExperienceSerializer(many=True, required=False)
    careers = CareerSerializer(many=True, required=False)

    class Meta:
        model = Resume
        fields = [
            "id","user","created_at","shablon_text",
            "personal_info","education","languages","experiences","careers",
        ]

    def create(self, validated_data):
        request = self.context.get("request")  
        user = request.user                   

        personal_info_data = validated_data.pop("personal_info", None)
        education_data = validated_data.pop("education", [])
        languages_data = validated_data.pop("languages", [])
        experiences_data = validated_data.pop("experiences", [])
        careers_data = validated_data.pop("careers", [])

        resume = Resume.objects.create(user=user, **validated_data)

        if personal_info_data:
            PersonalInfo.objects.create(resume=resume, **personal_info_data)

        for edu in education_data:
            Education.objects.create(resume=resume, **edu)

        for lang in languages_data:
            Language.objects.create(resume=resume, **lang)

        for exp in experiences_data:
            WorkExperience.objects.create(resume=resume, **exp)

        for car in careers_data:
            Career.objects.create(resume=resume, **car)

        return resume