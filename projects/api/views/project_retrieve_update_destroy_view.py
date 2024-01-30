from rest_framework.generics import RetrieveUpdateDestroyAPIView
from projects.api.serializers import ContentSerializer
from projects.models import ContentModel


class ProjectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContentSerializer
    queryset = ContentModel
    lookup_field = 'slug'

