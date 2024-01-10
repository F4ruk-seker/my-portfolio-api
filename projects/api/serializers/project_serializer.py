from rest_framework import serializers
from projects.models import ProjectModel


class ProjectSerializer(serializers.ModelSerializer):
    word_count = serializers.SerializerMethodField()

    @staticmethod
    def get_word_count(instance):
        return len(instance.context.split(' '))

    class Meta:
        model = ProjectModel
        fields = '__all__'


