from rest_framework.response import Response
from rest_framework.views import APIView
from analytical.api.serializers import PageYearlySerializer
from django.shortcuts import get_object_or_404
from pages.models import PageModel
from django.db.models import Count
from django.db.models.functions import ExtractMonth


class PageYearMonthlyView(APIView):

    def get(self, *args, **kwargs):
        page = get_object_or_404(PageModel, name=kwargs.get('name', None))
        views = (
                page.view
                .filter(visit_time__year=kwargs.get('year'))
                .annotate(month=ExtractMonth('visit_time'))
                .values('month')
                .annotate(count=Count('id'))
                .order_by('month')
        )
        apex = [0] * 12
        for view in views:
            apex[view['month'] - 1] = view['count']
        return Response(apex)
