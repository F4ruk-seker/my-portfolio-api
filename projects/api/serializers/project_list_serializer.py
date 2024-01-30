from .project_serializer import ContentSerializer
from projects.models import ContentModel

#
# @staticmethod
# def get_word_count(instance):
#     return len(instance.text.split(' ')) if instance.text else 0


class ContentListSerializer(ContentSerializer):
    class Meta:
        model = ContentModel
        fields = '__all__'
        # exclude = ('context',)

