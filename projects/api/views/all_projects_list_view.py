from rest_framework.generics import ListAPIView
from projects.api.serializers import ContentListSerializer
from projects.models import ContentModel
from rest_framework.filters import OrderingFilter, SearchFilter, BaseFilterBackend
from django.db.models import Q


class AllProjectsListView(ListAPIView):
    authentication_classes = []
    serializer_class = ContentListSerializer
    filter_backends: list = [SearchFilter, OrderingFilter]
    search_fields: tuple = 'title', 'content_type__name', 'tags__id'

    lookup_field = 'content_type'

    def get_queryset(self, *args, **kwargs):
        queryset = ContentModel.objects.filter(show=True)

        content_type_param = self.request.query_params.get('content_type')
        if content_type_param:
            queryset = queryset.filter(content_type__name=content_type_param)

        tags = self.request.query_params.get('tags')
        if tags:
            queryset = queryset.filter(Q(tags__id__in=[tag for tag in tags.split(',') if tag])).distinct()
        return queryset
