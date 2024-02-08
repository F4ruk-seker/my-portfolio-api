from rest_framework.generics import RetrieveUpdateDestroyAPIView
from todo.api.serializers import ToDoSerializer

from todo.models import ToDoModel


class ToDoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ToDoModel
    serializer_class = ToDoSerializer
    lookup_field: str = 'pk'

