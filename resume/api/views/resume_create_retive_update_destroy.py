from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from resume.models import ResumeModel
from resume.api.serializers import ResumeSerializer, ResumeEditSerializer


class ResumeView(RetrieveAPIView):
    serializer_class = ResumeSerializer
    lookup_field = 'user__username'
    authentication_classes = []

    def get_queryset(self, **kwargs):
        if lookup_field := self.kwargs[self.lookup_field]:
            return ResumeModel.objects.filter(**{self.lookup_field: lookup_field})


class ResumeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeEditSerializer
    lookup_field = 'user__username'
    authentication_classes = []

    def get_queryset(self, **kwargs):
        if lookup_field := self.kwargs[self.lookup_field]:
            return ResumeModel.objects.filter(**{self.lookup_field: lookup_field})




