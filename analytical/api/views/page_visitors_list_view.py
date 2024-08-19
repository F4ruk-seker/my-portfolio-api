from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from analytical.api.serializers import ViewSerializer
from pages.models import PageModel
from django.shortcuts import get_object_or_404


class VisitorsResultsPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'results_size'
    max_page_size = 100


class PageVisitorsListView(ListAPIView):
    lookup_field = 'name'
    serializer_class = ViewSerializer
    filter_backends: list = SearchFilter, OrderingFilter
    search_fields: list = 'user_agent', 'ip_address', 'user_agent'
    ordering_fields: list = 'visit_time', 'reload_count_in_a_clock'
    pagination_class = VisitorsResultsPageNumberPagination

    def get(self, request, *args, **kwargs):
        page_model: PageModel = get_object_or_404(PageModel, **{self.lookup_field: kwargs.get(self.lookup_field)})
        views = page_model.get_view()
        self.queryset = views
        return super().get(request, *args, **kwargs)
