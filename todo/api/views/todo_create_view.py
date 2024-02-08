from rest_framework.generics import CreateAPIView
from todo.api.serializers import ToDoSerializer
from todo.models import ToDoModel


class ToDoCreateView(CreateAPIView):
    queryset = ToDoModel
    serializer_class = ToDoSerializer
