from rest_framework.generics import RetrieveUpdateDestroyAPIView
from todo.models import ToDoCategoryModel
from todo.api.serializers import ToDoCategorySerializer


class ToDoCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoCategorySerializer
    queryset = ToDoCategoryModel.objects.all()
