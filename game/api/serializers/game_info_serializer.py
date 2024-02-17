from rest_framework import serializers
from game.models import GameInfoModel


class GameInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameInfoModel
        fields: str = '__all__'

