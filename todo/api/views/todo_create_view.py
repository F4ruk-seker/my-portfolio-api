from rest_framework.generics import CreateAPIView
from todo.api.serializers import ToDoSerializer
from todo.models import ToDoModel, ToDoCategoryModel
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_206_PARTIAL_CONTENT


class ToDoCreateView(CreateAPIView):
    queryset = ToDoModel
    serializer_class = ToDoSerializer
