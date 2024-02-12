from rest_framework.generics import RetrieveAPIView
from projects.api.serializers import ContentSerializer
from projects.models import ContentModel


class ProjectRetrieveView(RetrieveAPIView):
    authentication_classes = []
    serializer_class = ContentSerializer
    # queryset = ContentModel.objects.filter(show=True)
    lookup_field = 'slug'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ContentModel.objects.all()
        return ContentModel.objects.filter(show=True)

