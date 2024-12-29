from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from analytical.api.serializers import AnalyticalMediaSerializer
from analytical.models import AnalyticMedia
from rest_framework.filters import OrderingFilter, SearchFilter


class AnalyticalMediaListCreateView(ListCreateAPIView):
    serializer_class = AnalyticalMediaSerializer
    filter_backends: list = [SearchFilter, OrderingFilter]
    search_fields: tuple = 'title', 'view__ip_address', 'media_source', 'slug', 'platform_host'
    ordering_fields: tuple = 'title', 'platform_host', 'created_at', 'updated_at'
    permission_classes = [
        IsAuthenticated, IsAdminUser
    ]

    def get_queryset(self):
        return AnalyticMedia.objects.all().order_by('platform_host')
