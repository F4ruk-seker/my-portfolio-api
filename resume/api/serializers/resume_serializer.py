from rest_framework import serializers
from resume.models import ResumeModel
import markdown_to_json


class ResumeSerializer(serializers.ModelSerializer):
    context = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_context(instance):
        return markdown_to_json.dictify(instance.context)

    class Meta:
        model = ResumeModel
        exclude: tuple = 'user',


class ResumeEditSerializer(serializers.ModelSerializer):
    marked = serializers.SerializerMethodField(read_only=True, required=False)

    @staticmethod
    def get_marked(instance):
        return markdown_to_json.dictify(instance.context)

    class Meta:
        model = ResumeModel
        exclude: tuple = 'user',
