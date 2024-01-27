from rest_framework import serializers
from projects.models import ProjectModel
from tags.api.serializers import ProgramingLanguageSerializer, ToolSerializers


class ProjectSerializer(serializers.ModelSerializer):
    word_count = serializers.SerializerMethodField()
    programing_languages = ProgramingLanguageSerializer(many=True)
    used_tools = ToolSerializers(many=True)

    @staticmethod
    def get_word_count(instance):
        return len(instance.context.split(' ')) if instance.context else 0
        # return '0'

    class Meta:
        model = ProjectModel
        fields = '__all__'


