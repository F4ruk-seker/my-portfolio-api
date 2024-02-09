from .project_serializer import ContentSerializer
from projects.models import ContentModel
from rest_framework import serializers

#
# @staticmethod
# def get_word_count(instance):
#     return len(instance.text.split(' ')) if instance.text else 0


class ContentListSerializer(ContentSerializer):
    update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = ContentModel
        # fields = '__all__'
        exclude = ('text',)

