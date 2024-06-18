from rest_framework import serializers
from todo.models import ToDoCategoryModel
from todo.api.serializers import ToDoSerializer


class ToDoCategorySerializer(serializers.ModelSerializer):
    # death_of_line = serializers.DateField()
    todos = serializers.SerializerMethodField(read_only=True)
    is_done = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_todos(instance):
        return ToDoSerializer(instance.all_todos.order_by('-created').order_by('is_to_do'), many=True).data

    @staticmethod
    def get_is_done(instance):
        return instance.is_end

    class Meta:
        model = ToDoCategoryModel
        fields: str = '__all__'
        # fields: tuple = 'title', 'todos'
        # exclude: tuple = 'created',
