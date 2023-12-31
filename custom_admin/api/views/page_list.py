from rest_framework.generics import ListCreateAPIView
from custom_admin.api.serializers import PageListSerializer

from pages.models import PageModel


class PageListView(ListCreateAPIView):
    serializer_class = PageListSerializer
    queryset = PageModel.objects.all()

