from rest_framework import serializers
from analytical.api.serializers import ViewSerializer
from analytical.utils import ViewCountWithRule
from message.models import MessageModel


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields: tuple = 'name', 'email', 'message'
        extra_kwargs = {'view': {'write_only': True}}

    def create(self, validated_data):
        counter = ViewCountWithRule(None, self.context['request'])
        validated_data['view'] = counter.create_view()
        message = super(MessageCreateSerializer, self).create(validated_data)
        return message


class MessageReaderSerializer(serializers.ModelSerializer):
    view = ViewSerializer()

    class Meta:
        model = MessageModel
        fields: str = '__all__'

