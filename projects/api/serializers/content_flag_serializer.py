from rest_framework.serializers import ModelSerializer
from projects.models import ContentTypeModel
from tags.api.serializers import TagCategorySerializer


class ContentTypeSerializer(ModelSerializer):
    sub_tags = TagCategorySerializer(many=True)

    def to_representation(self, instance):
        # Serialize the instance
        data = super().to_representation(instance)

        # Sort the 'sub_tags' based on the 'order' field
        data['sub_tags'] = sorted(data['sub_tags'], key=lambda x: x['order'])

        return data

    class Meta:
        model = ContentTypeModel
        fields: str = '__all__'
