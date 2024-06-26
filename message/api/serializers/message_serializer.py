from rest_framework import serializers
from analytical.api.serializers import ViewSerializer
from analytical.utils import ViewCountWithRule
from message.models import MessageModel


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields: tuple = 'name', 'email', 'message'
        extra_kwargs = {'sender_agent': {'write_only': True}}

    def create(self, validated_data):
        counter = ViewCountWithRule(None, self.context['request'])
        validated_data['sender_agent'] = counter.create_view()
        message = super(MessageCreateSerializer, self).create(validated_data)
        return message


class MessageReaderSerializer(serializers.ModelSerializer):
    sender_agent = ViewSerializer()

    class Meta:
        model = MessageModel
        fields: str = '__all__'

