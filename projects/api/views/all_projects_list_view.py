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
    # queryset = ContentModel.objects.all()
    filter_backends: list = [SearchFilter, OrderingFilter]
    search_fields: tuple = 'slug', 'title', 'programing_languages__name'
    lookup_field = 'content_type'

    def get_queryset(self, content_type):
        query: dict = {
            'content_type__name': content_type,

        }
        if tags := self.request.query_params.get('tags'):
            tags.split(',')

            # return ContentModel.objects.filter(content_type__name='project', tags__in=tags).all()
        # else:
        #     return ContentModel.objects.filter(content_type__name='project').all()
        return ContentModel.objects.filter(**query).all()

    def list(self, request, *args, **kwargs):
        content_type = kwargs.get('content_type')
        serializer = self.get_serializer(self.get_queryset(content_type), many=True)
        # filter_keys: dict = {
        #     'tags': TagCategorySerializer(instance=TagCategoryModel.objects.all(), many=True).data,
        # }

        return Response(serializer.data)

