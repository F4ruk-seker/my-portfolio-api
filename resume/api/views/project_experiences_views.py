from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import CreateAPIView
from resume.api.serializers import ProjectExperiencesSerializer
from resume.models import ProjectExperiencesModel


class ProjectExperiencesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectExperiencesSerializer
    lookup_field = 'pk'
    queryset = ProjectExperiencesModel.objects.all()


class ProjectExperiencesCreateView(CreateAPIView):
    serializer_class = ProjectExperiencesSerializer

