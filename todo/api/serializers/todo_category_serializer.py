from rest_framework import serializers
from todo.models import ToDoCategoryModel


class ToDoSerializer(serializers.ModelSerializer):
    todos = serializers.SerializerMethodField()

    @staticmethod
    def get_todos(instance):
        return instance.all_todos()

    class Meta:
        model = ToDoCategoryModel
        fields: str = '__all__'

