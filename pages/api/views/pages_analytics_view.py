from pages.models import PageModel
from rest_framework.generics import ListAPIView

from pages.api.serializers import PagesAnalyticsSerializer


class PagesAnalyticsView(ListAPIView):
    serializer_class = PagesAnalyticsSerializer
    queryset = PageModel.objects.all()

