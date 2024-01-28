from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from projects.api.serializers import ProjectListSerializer
from projects.models import ProjectModel
from rest_framework.filters import OrderingFilter, SearchFilter, BaseFilterBackend
from tags.models import ToolModel, ProgramingLanguageModel
from tags.api.serializers import ProgramingLanguageSerializer, ToolSerializer


class AllProjectsListView(ListAPIView):
    authentication_classes = []
    serializer_class = ProjectListSerializer
    queryset = ProjectModel.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = 'slug', 'title', 'programing_languages__name'

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        result: dict = serializer.data
        filter_keys: dict = {
            'languages': ProgramingLanguageSerializer(instance=ProgramingLanguageModel.objects.all(), many=1).data,
            'tools': ToolSerializer(instance=ToolModel.objects.all(), many=1).data,
        }

        return Response({'result': result, 'filter_keys': filter_keys})

