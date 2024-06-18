from rest_framework.generics import CreateAPIView
from todo.api.serializers import ToDoCategorySerializer
from todo.models import ToDoCategoryModel


class ToDoCategoryCreateView(CreateAPIView):
    queryset = ToDoCategoryModel
    serializer_class = ToDoCategorySerializer
    