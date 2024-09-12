from rest_framework.generics import RetrieveUpdateDestroyAPIView
from analytical.api.serializers import AnalyticalMediaSerializer
from analytical.models import AnalyticMedia


class AnalyticalMediaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnalyticalMediaSerializer
    queryset = AnalyticMedia.objects.all()
    lookup_field = 'pk'
    
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
