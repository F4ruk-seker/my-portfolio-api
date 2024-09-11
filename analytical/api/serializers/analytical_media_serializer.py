from rest_framework import serializers
from analytical.models import AnalyticMedia
from analytical.api.serializers.view_serializer import ViewSerializer


class AnalyticalMediaSerializer(serializers.ModelSerializer):
    view = ViewSerializer(many=True, required=False)

    class Meta:
        model = AnalyticMedia
        fields: str = '__all__'
