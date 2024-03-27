from rest_framework import serializers
from analytical.models import ViewModel


class ViewSerializer(serializers.ModelSerializer):
    current_time = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_current_time(instance):
        return instance.get_ticked_time()

    class Meta:
        model = ViewModel
        fields: str = '__all__'
