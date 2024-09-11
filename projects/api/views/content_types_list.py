from rest_framework.generics import ListCreateAPIView
from projects.models import ContentTypeModel
from projects.api.serializers import ContentTypeSerializer


class ContentsView(ListCreateAPIView):
    queryset = ContentTypeModel.objects.all()
    serializer_class = ContentTypeSerializer
    authentication_classes = []
