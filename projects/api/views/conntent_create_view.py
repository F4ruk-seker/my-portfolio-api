from rest_framework.generics import CreateAPIView

from projects.api.serializers import ContentSerializer


class ContentCreateView(CreateAPIView):
    serializer_class = ContentSerializer


