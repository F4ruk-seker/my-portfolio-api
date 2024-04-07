from rest_framework.generics import CreateAPIView
from message.models import MessageModel
from message.api.serializers import MessageCreateSerializer
from analytical.utils import ViewCountWithRule


class CreateMessageView(CreateAPIView):
    model = MessageModel
    serializer_class = MessageCreateSerializer
    authentication_classes = []

    # def create(self, request, *args, **kwargs):
    #     counter = ViewCountWithRule(None, self.request)
    #     sender_agent = counter.create_view()
    #     request.data['sender_agent'] = sender_agent.id
    #     print("redm")
    #     return super().create(request, *args, **kwargs)