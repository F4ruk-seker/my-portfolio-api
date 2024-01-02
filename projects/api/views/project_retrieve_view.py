from rest_framework.generics import RetrieveAPIView
from projects.api.serializers import ProjectSerializer
from projects.models import ProjectModel


class ProjectRetrieveView(RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = ProjectModel
    lookup_field = 'slug'

