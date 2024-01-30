from rest_framework import serializers
from projects.models import ContentModel
from tags.api.serializers.tag_serializer import TagSerializer


class ContentSerializer(serializers.ModelSerializer):
    # programing_languages = TagSerializer(many=True, required=False)
    # used_tools = TagSerializer(many=True, required=False)
    # context = ContextSerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)

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

