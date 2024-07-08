from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import ExtractHour

from pages.models import PageModel


class PageMonthDayView(APIView):
    def get(self, *args, **kwargs):
        page = get_object_or_404(PageModel, name=kwargs.get('name', None))

        # 2024 Ocak ayının 10. günündeki view'ları saatlere göre gruplayarak sayan sorgu
        views_per_hour_10_jan_2024 = (
            page.get_view()
            .filter(
                visit_time__year=kwargs.get('year'),
                visit_time__month=kwargs.get('month'),
                visit_time__day=kwargs.get('day')
            )
            .annotate(hour=ExtractHour('visit_time'))
            .values('hour')
            .annotate(count=Count('id'))
            .order_by('hour')
        )

        # 10. gündeki tüm saatler için default 0 değerleri ile bir liste oluşturma (24 saat)
        apex_hours = [0] * 24

        # Sorgu sonuçlarını listeye aktarma
        for view in views_per_hour_10_jan_2024:
            hour_index = view['hour']
            apex_hours[hour_index] = view['count']

        return Response(apex_hours)
