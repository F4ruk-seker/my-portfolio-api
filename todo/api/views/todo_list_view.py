from rest_framework.generics import ListAPIView
from todo.models import ToDoModel, ToDoCategoryModel
from todo.api.serializers import ToDoSerializer, ToDoCategorySerializer


class AllToDoListView(ListAPIView):
    # queryset = ToDoModel.objects.all().order_by('-created').order_by('is_to_do')
    serializer_class = ToDoCategorySerializer

    def get_queryset(self):
        return ToDoCategoryModel.objects.all()