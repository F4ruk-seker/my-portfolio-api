from rest_framework.generics import RetrieveAPIView
from projects.models import ContentTypeModel
from projects.api.serializers import ContentTypeSerializer


class ContentFlagsView(RetrieveAPIView):
    authentication_classes = []
    lookup_field = 'name'
    queryset = ContentTypeModel
    serializer_class = ContentTypeSerializer

