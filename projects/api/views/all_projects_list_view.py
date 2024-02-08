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
    filter_backends: list = [SearchFilter, OrderingFilter]
    search_fields: tuple = 'title', 'content_type__name', 'tags__name'

    lookup_field = 'content_type'
    # queryset = ContentModel.objects

    def get_queryset(self, *args, **kwargs):
        queryset = ContentModel.objects.all()

        content_type_param = self.request.query_params.get('content_type')
        if content_type_param:
            queryset = queryset.filter(content_type__name=content_type_param)

        tags = self.request.query_params.get('tags')
        if tags:
            tag_list = tags.split(',')
            queryset = queryset.filter(tags__name__in=tag_list)

        return queryset
    # def get_queryset(self, content_type='', *args, **kwargs):

        # if queryset := super().get_queryset():
        #     query: dict = {
        #         'content_type__name': content_type,
        #     }
        #     if tags := self.request.query_params.get('tags'):
        #         query['tags__in'] = [tag_id for tag_id in tags.split(',') if tag_id]
        #         return queryset.objects.filter(**query).all()

    # def list(self, request, *args, **kwargs):
    #     content_type = kwargs.get('content_type')
    #     serializer = self.get_serializer(self.get_queryset(content_type=content_type), many=True)
    #     return Response(serializer.data)
    #
