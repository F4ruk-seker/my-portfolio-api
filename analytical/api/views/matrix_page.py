from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from analytical.api.serializers import PageYearlySerializer
from django.shortcuts import get_object_or_404
from pages.models import PageModel
from django.db.models import Count
from django.db.models.functions import ExtractYear


class PageYearlyView(APIView):
    serializer_class = PageYearlySerializer
    lookup_field = 'name'
    permission_classes = [
        IsAuthenticated, IsAdminUser
    ]

    def get_queryset(self):
        page = get_object_or_404(PageModel, name=self.kwargs.get('name', None))
        return page.view.annotate(year=ExtractYear('visit_time')).values('year').annotate(
            count=Count('id')).order_by('year')

    def get(self, *args, **kwargs):
        return Response(PageYearlySerializer(self.get_queryset(), many=True).data)
