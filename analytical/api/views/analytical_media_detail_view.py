from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from analytical.api.serializers import AnalyticalMediaSerializer
from analytical.models import AnalyticMedia


class AnalyticalMediaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnalyticalMediaSerializer
    queryset = AnalyticMedia.objects.all()
    lookup_field = 'pk'
    permission_classes = [
        IsAuthenticated, IsAdminUser
    ]

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
