from resume.models import WorkExperiencesModel
from rest_framework import serializers


class WorkExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperiencesModel
        fields: str = '__all__'

