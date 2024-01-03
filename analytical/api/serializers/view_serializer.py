from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import serializers
from analytical.models import ViewModel
from django.conf import settings

if settings.DEBUG:
    class ViewSerializer(serializers.ModelSerializer):
        class Meta:
            model = ViewModel
            fields = '__all__'

else:
    @method_decorator(cache_page(60 * 15), name='list')  # Cache the list view for 15 minutes
    class ViewSerializer(serializers.ModelSerializer):
        class Meta:
            model = ViewModel
            fields = '__all__'
