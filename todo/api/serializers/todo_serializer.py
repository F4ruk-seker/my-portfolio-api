from rest_framework.serializers import ModelSerializer
from todo.models import ToDoModel


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDoModel
        # fields: str = '__all__'
        # exclude: tuple = 'created', 'category'
        exclude: tuple = 'category',


