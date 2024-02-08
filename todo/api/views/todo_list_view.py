from rest_framework.generics import ListAPIView
from todo.models import ToDoModel
from todo.api.serializers import ToDoSerializer


class AllToDoListView(ListAPIView):
    queryset = ToDoModel.objects.all().order_by('-created').order_by('is_to_do')
    serializer_class = ToDoSerializer

