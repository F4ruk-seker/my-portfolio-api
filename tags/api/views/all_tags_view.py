from rest_framework.response import Response
from rest_framework.views import APIView
from tags.api import serializers as tags_serializers
from tags import models


class AllTagsListView(APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        tags = dir(models)
        result: dict = {}
        for tag in tags:
            if tag.endswith('Model'):
                serializer = getattr(tags_serializers, tag.replace('Model', 'Serializer'))
                result[tag] = serializer(instance=getattr(models, tag).objects.all(), many=True).data
        return Response(result)

