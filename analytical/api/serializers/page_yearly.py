from rest_framework import serializers


class PageYearlySerializer(serializers.Serializer):
    year = serializers.CharField(max_length=4)
    count = serializers.CharField(max_length=25)
