from rest_framework.serializers import ModelSerializer
from projects.models import ContentTypeModel
from tags.api.serializers import TagCategorySerializer


class ContentTypeSerializer(ModelSerializer):
    sub_tags = TagCategorySerializer(many=True)

    class Meta:
        model = ContentTypeModel
        fields: str = '__all__'
