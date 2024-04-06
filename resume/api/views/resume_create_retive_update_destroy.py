from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from resume.models import ResumeModel
from resume.api.serializers import ResumeAlpha
from django.shortcuts import get_object_or_404


class ResumeView(RetrieveAPIView):
    lookup_field = None
    serializer_class = ResumeAlpha

    def get_object(self):
        return get_object_or_404(ResumeModel, pk=1)


class ResumeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_field = None
    serializer_class = ResumeAlpha

    def get_queryset(self):
        return ResumeModel.objects.all()

    def get_object(self):
        return get_object_or_404(ResumeModel, pk=1)


