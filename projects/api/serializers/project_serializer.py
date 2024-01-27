from rest_framework import serializers
from projects.models import ProjectModel
from tags.api.serializers import ProgramingLanguageSerializer, ToolSerializers


class ProjectSerializer(serializers.ModelSerializer):
    word_count = serializers.SerializerMethodField(required=False, read_only=True)
    programing_languages = ProgramingLanguageSerializer(many=True, required=False)
    used_tools = ToolSerializers(many=True, required=False)

    @staticmethod
    def get_word_count(instance):
        return len(instance.context.split(' ')) if instance.context else 0
        # return '0'

    class Meta:
        model = ProjectModel
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('word_count', None)
        validated_data.pop('programing_languages', None)
        validated_data.pop('used_tools', None)

        # Your custom logic for updating the instance with the nested data

        instance = super().update(instance, validated_data)
        return instance