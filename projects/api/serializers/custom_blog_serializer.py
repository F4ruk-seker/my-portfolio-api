from rest_framework import serializers
from .project_serializer import ContentSerializer


class CustomBLogContentSerializer(serializers.Serializer):
    contents = ContentSerializer(many=True)
    trends = ContentSerializer(many=True)
    featured = ContentSerializer(many=True)
