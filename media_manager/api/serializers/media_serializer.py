from rest_framework import serializers
from media_manager.models import MediaModel


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaModel
        fields: str = '__all__'

