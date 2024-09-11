from rest_framework.generics import ListCreateAPIView
from analytical.api.serializers import AnalyticalMediaSerializer
from analytical.models import AnalyticMedia


class AnalyticalMediaListCreateView(ListCreateAPIView):
    serializer_class = AnalyticalMediaSerializer
    queryset = AnalyticMedia.objects.all()
