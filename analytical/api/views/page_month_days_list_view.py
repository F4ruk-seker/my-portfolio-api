from django.db.models import Count
from django.db.models.functions import ExtractDay
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from pages.models import PageModel


class PageMonthDaysListView(APIView):
    def get(self, request, *args, **kwargs):
        page = get_object_or_404(PageModel, name=kwargs.get('name', None))
        views_per_day_jan_2024 = (
            page.get_view()
            .filter(
                visit_time__year=kwargs.get('year'),
                visit_time__month=kwargs.get('month')
            )
            .annotate(day=ExtractDay('visit_time'))
            .values('day')
            .annotate(count=Count('id'))
            .order_by('day')
        )

        # Ocak ayındaki tüm günler için default 0 değerleri ile bir liste oluşturma (31 gün)
        apex_days = [0] * 31

        # Sorgu sonuçlarını listeye aktarma
        for view in views_per_day_jan_2024:
            day_index = view['day'] - 1  # Günler 1'den başlar
            apex_days[day_index] = view['count']

        # <name>/<int:year>/<int:month>
        return Response(apex_days)
    ...

