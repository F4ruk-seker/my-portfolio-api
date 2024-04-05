from rest_framework.generics import ListAPIView
from analytical.api.serializers import ItemSerializer

from projects.models import ContentModel
from pages.models import PageModel


class Items(ListAPIView):
    serializer_class = ItemSerializer
    items: list = PageModel, ContentModel

    def get_items(self):
        return getattr(self, 'items')

    def get_queryset(self):
        return [children for item in [item.objects.all() for item in self.get_items()] for children in item]

