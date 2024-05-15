from resume.models import ProjectExperiencesModel
from rest_framework import serializers


class ProjectExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectExperiencesModel
        fields: str = '__all__'

