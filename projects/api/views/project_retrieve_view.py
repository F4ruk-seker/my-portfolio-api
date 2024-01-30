from rest_framework.generics import RetrieveAPIView
from projects.api.serializers import ContentSerializer
from projects.models import ContentModel


class ProjectRetrieveView(RetrieveAPIView):
    authentication_classes = []
    serializer_class = ContentSerializer
    queryset = ContentModel
    lookup_field = 'slug'

