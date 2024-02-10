from rest_framework import serializers

from .comment_serializer import ContentCommentSerializer
from projects.models import ContentModel
from tags.api.serializers.tag_serializer import TagSerializer


class ContentSerializer(serializers.ModelSerializer):
    word_count = serializers.SerializerMethodField(required=False, read_only=True)
    # programing_languages = TagSerializer(many=True, required=False)
    # used_tools = TagSerializer(many=True, required=False)
    # context = ContextSerializer(many=True, required=False)
    comments = ContentCommentSerializer(many=True)
    tags = TagSerializer(many=True, required=False)

    @staticmethod
    def get_word_count(instance):
        return len(instance.text.split(' ')) if instance.text else 0

    class Meta:
        model = ContentModel
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('word_count', None)
        validated_data.pop('programing_languages', None)
        validated_data.pop('used_tools', None)
        validated_data.pop('tags', None)

        instance = super().update(instance, validated_data)
        return instance

