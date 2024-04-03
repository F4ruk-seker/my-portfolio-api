from rest_framework.generics import RetrieveUpdateDestroyAPIView
from projects.api.serializers import ContentSerializer
from projects.models import ContentModel
from tags.models import TagModel


class ProjectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContentSerializer
    queryset = ContentModel.objects.all()
    lookup_field = 'slug'
