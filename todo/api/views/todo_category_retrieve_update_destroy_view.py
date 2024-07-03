from rest_framework.generics import RetrieveUpdateDestroyAPIView
from todo.models import ToDoCategoryModel
from todo.api.serializers import ToDoCategorySerializer


class ToDoCategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoCategorySerializer
    queryset = ToDoCategoryModel.objects.all()

# webhook = SyncWebhook.from_url(
# "https://discord.com/api/webhooks/1252903405941293116/8Nry4N_0OXludQjttaeOIcEkKObS_IOED0T9ruNufkcnnCQ7kM1tnEV8Xmh9xZ_2LzB0")
# webhook.send(':bell: Attention: Last day for "Task Manage APP", 19.06.2024')
# webhook.send(':white_check_mark: Completion "Task Manage APP" completed')
# print(webhook.channel.members)

