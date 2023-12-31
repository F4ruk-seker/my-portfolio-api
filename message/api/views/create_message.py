from rest_framework.generics import CreateAPIView
from message.models import MessageModel
from message.api.serializers import MessageSerializer


class CreateMessageView(CreateAPIView):
    model = MessageModel
    serializer_class = MessageSerializer
    authentication_classes = []

