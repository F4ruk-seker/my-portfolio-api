from rest_framework.generics import RetrieveUpdateDestroyAPIView
from pages.api.serializers import PageAdminSerializer
from pages.models import PageModel


class PageManageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PageAdminSerializer
    lookup_field = 'name'
    queryset = PageModel

