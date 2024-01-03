from pages.models import PageModel
from rest_framework.generics import RetrieveAPIView

from pages.api.serializers import PagesAnalyticsSerializer


class PagesAnalyticsView(RetrieveAPIView):
    serializer_class = PagesAnalyticsSerializer
    queryset = PageModel.objects.all()
    lookup_field = 'name'

