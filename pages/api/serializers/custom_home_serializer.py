from rest_framework.serializers import Serializer
from projects.api.serializers import ContentSerializer


class CustomHomeSerializer(Serializer):
    featured_projects = ContentSerializer(many=True)
    featured_blogs = ContentSerializer(many=True)

