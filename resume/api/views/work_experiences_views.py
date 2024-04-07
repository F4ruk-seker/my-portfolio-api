from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import CreateAPIView

from resume.api.serializers import WorkExperiencesSerializer
from resume.models import WorkExperiencesModel


class WorkExperiencesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkExperiencesSerializer
    lookup_field = 'pk'
    queryset = WorkExperiencesModel.objects.all()


class WorkExperiencesCreateView(CreateAPIView):
    serializer_class = WorkExperiencesSerializer

