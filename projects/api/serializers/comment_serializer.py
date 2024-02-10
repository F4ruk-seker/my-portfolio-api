from projects.models import ContentCommentModel
from rest_framework import serializers


class ContentCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(required=False)
    comment = serializers.CharField(max_length=500)

    @staticmethod
    def get_user(obj):
        if user := obj.user:
            return user.username
        return None

    class Meta:
        model = ContentCommentModel
        fields: str = '__all__'

