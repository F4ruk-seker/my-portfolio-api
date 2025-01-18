from rest_framework.generics import RetrieveUpdateDestroyAPIView
from todo.models import ToDoCategoryModel
from todo.api.serializers import ToDoCategorySerializer


class ToDoCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoCategorySerializer
    queryset = ToDoCategoryModel.objects.all()

# webhook = SyncWebhook.from_url("<Token>")
# webhook.send(':bell: Attention: Last day for "Task Manage APP", 19.06.2024')
# webhook.send(':white_check_mark: Completion "Task Manage APP" completed')
# print(webhook.channel.members)

