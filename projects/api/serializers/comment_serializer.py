from projects.models import ContentCommentModel
from rest_framework import serializers
from analytical.utils import ViewCountWithRule


class ContentCommentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        if self.context:
            counter = ViewCountWithRule(None, self.context['request'])
            validated_data['sender_agent'] = counter.create_view()
        return super().create(validated_data)

    class Meta:
        model = ContentCommentModel
        # fields: str = '__all__'
        exclude: tuple = 'sender_agent',
