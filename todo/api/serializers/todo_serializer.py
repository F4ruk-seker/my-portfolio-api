from rest_framework import serializers
from todo.models import ToDoModel


class ToDoSerializer(serializers.ModelSerializer):
    # created = serializers.DateTimeField(format="%d.%m.%YT%H:%M:%S")

    # @staticmethod
    # def created(obj):
    #     return {
    #
    #     }

    class Meta:
        model = ToDoModel
        fields: str = '__all__'
        # exclude: tuple = 'created', 'category'
        # exclude: tuple = 'category',


