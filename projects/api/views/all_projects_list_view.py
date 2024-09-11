from rest_framework.generics import ListCreateAPIView
from projects.api.serializers import ContentListSerializer
from projects.models import ContentModel
from rest_framework.filters import OrderingFilter, SearchFilter, BaseFilterBackend
from django.db.models import Q


class AllProjectsListView(ListCreateAPIView):
    serializer_class = ContentListSerializer
    filter_backends: list = [SearchFilter, OrderingFilter]
    search_fields: tuple = 'title', 'content_type__name', 'tags__id'
    lookup_field = 'content_type'
    authentication_classes = []

    def get_queryset(self, *args, **kwargs):

        queryset = ContentModel.objects.filter(show=True)

        content_type_param = self.request.query_params.get('content_type')
        if content_type_param:
            queryset = queryset.filter(content_type__name=content_type_param)

        tags = self.request.query_params.get('tags')
        if tags:
            queryset = queryset.filter(Q(tags__id__in=[tag for tag in tags.split(',') if tag])).distinct()

        if latest := self.request.query_params.get('latest'):
            queryset = queryset.order_by('-update')[:int(latest)]

        if lang := self.request.query_params.get('lang'):
            if lang in ContentModel.LanguageType.values:
                queryset = queryset.filter(Q(language_type=lang))
        return queryset
