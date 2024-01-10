from .project_serializer import ProjectSerializer
from projects.models import ProjectModel
from rest_framework import serializers


class ProjectListSerializer(ProjectSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'
        # exclude = ('context',)

