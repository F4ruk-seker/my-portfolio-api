from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from projects.api.serializers import ContentListSerializer
from projects.models import ContentModel
from rest_framework.filters import OrderingFilter, SearchFilter, BaseFilterBackend
from tags.models import TagCategoryModel
from tags.api.serializers import TagCategorySerializer


class AllProjectsListView(ListAPIView):
    authentication_classes = []
    serializer_class = ContentListSerializer
    queryset = ContentModel.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = 'slug', 'title', 'programing_languages__name'

    def get_queryset(self):
        return ContentModel.objects.filter(content_type__name='project').all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        result: dict = serializer.data
        filter_keys: dict = {
            'tags': TagCategorySerializer(instance=TagCategoryModel.objects.all(), many=True).data,
        }

        return Response({'result': result, 'filter_keys': filter_keys})

