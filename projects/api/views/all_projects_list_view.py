from rest_framework.generics import ListAPIView
from projects.api.serializers import ProjectListSerializer
from projects.models import ProjectModel
from rest_framework.filters import OrderingFilter, SearchFilter, BaseFilterBackend


class AllProjectsListView(ListAPIView):
    serializer_class = ProjectListSerializer
    queryset = ProjectModel.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = 'slug', 'title', 'programing_languages__name'


