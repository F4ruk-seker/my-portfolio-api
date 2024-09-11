from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin
from analytical.api.serializers import AnalyticalMediaSerializer
from analytical.models import AnalyticMedia


class AnalyticalMediaRetrieveDestroyView(RetrieveAPIView, DestroyModelMixin):
    serializer_class = AnalyticalMediaSerializer
    queryset = AnalyticMedia.objects.all()
    lookup_field = 'pk'
    
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)