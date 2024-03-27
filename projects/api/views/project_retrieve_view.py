from rest_framework.generics import RetrieveAPIView
from analytical.utils import ViewCountWithRule
from projects.api.serializers import ContentSerializer
from projects.models import ContentModel
from django.conf import settings


class ProjectRetrieveView(RetrieveAPIView):
    authentication_classes = []
    serializer_class = ContentSerializer
    # queryset = ContentModel.objects.filter(show=True)
    lookup_field = 'slug'

    def get_object(self):
        obj = super().get_object()
        view = ViewCountWithRule(obj, self.request, not settings.DEBUG)
        obj.ticket = view().id
        return obj

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ContentModel.objects.all()
        return ContentModel.objects.filter(show=True)

    # def get(self, *args, **kwargs):
    #     response = super().get(*args, **kwargs)
    #     response.data['extra'] = 'extra'
    #     return response

