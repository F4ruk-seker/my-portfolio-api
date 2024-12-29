from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from analytical.api.serializers import PageYearlySerializer
from django.shortcuts import get_object_or_404
from pages.models import PageModel
from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractDay


class PageYearMonthlyView(APIView):
    permission_classes = [
        IsAuthenticated, IsAdminUser
    ]

    def get(self, *args, **kwargs):
        page = get_object_or_404(PageModel, name=kwargs.get('name', None))

        # Fetch monthly visit counts
        monthly_views = (
            page.get_view()
            .filter(visit_time__year=kwargs.get('year'))
            .annotate(month=ExtractMonth('visit_time'), day=ExtractDay('visit_time'))
            .values('month', 'day')
            .annotate(count=Count('id'))
            .order_by('month', 'day')
        )
        # Prepare structure for monthly and daily counts
        apex = [[0] * 31 for _ in range(12)]  # Assuming maximum of 31 days in any month
        # Fill apex with monthly and daily counts
        for view in monthly_views:
            month_index = view['month'] - 1
            day_index = view['day'] - 1  # Adjust for 0-based index
            apex[month_index][day_index] = view['count']

        # Return response containing monthly and daily counts
        return Response(apex)

