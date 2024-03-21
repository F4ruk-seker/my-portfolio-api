from rest_framework import serializers
from analytical.models import ViewModel


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewModel
        fields: str = '__all__'
