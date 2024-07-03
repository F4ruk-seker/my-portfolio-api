from django.db.models import Count
from django.db.models.functions import ExtractDay
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from pages.models import PageModel
from rest_framework.exceptions import APIException

class PageMonthDaysView(APIView):
    def get(self, *args, **kwargs):
        result = ''
        try:
            # month
            page = get_object_or_404(PageModel, name=kwargs.get('name', None))
            year = kwargs.get('year')
            month = kwargs.get('month')

            views_per_day_jan_2024 = (
                page.view
                .filter(visit_time__year=year, visit_time__month=month)
                .annotate(day=ExtractDay('visit_time'))
                .values('day')
                .annotate(count=Count('id'))
                .order_by('day')
            )
            apx = []
            week = [0] * 7
            for _ in range(1, 31):
                for day in views_per_day_jan_2024:
                    if _ == day.get('day'):
                        result = f'_={_} / (len(apx) * 7) = {(len(apx) * 7)}'
                        week[_ - (len(apx) * 7)] = day.get('count')
                        break
                if _ % 7 == 0:
                    apx.append({
                        'name': f'week {len(apx) + 1}',
                        'data': week
                    })
                    week = [0] * 7
            if len(week) > 0:
                apx.append({
                    'name': f'week {len(apx) + 1}',
                    'data': week
                })
            return Response(apx)
        except Exception as exception:
            raise APIException(
                f'{result}\n' + str(exception)
            )

