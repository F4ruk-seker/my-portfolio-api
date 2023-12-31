from pages.models import PageModel
from rest_framework import serializers


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageModel
        fields = ('name', 'image', 'title')

