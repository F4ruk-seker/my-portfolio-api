from rest_framework.generics import RetrieveUpdateDestroyAPIView
from projects.api.serializers import ProjectSerializer
from projects.models import ProjectModel


class ProjectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = ProjectModel
    lookup_field = 'slug'

