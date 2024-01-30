from tags.models import TagModel
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class TagSerializer(ModelSerializer):
    category = SerializerMethodField()

    @staticmethod
    def get_category(obj):
        return obj.category.name

    class Meta:
        model = TagModel
        fields: str = '__all__'

