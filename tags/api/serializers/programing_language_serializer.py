from rest_framework.serializers import ModelSerializer
from tags.models import ProgramingLanguageModel


class ProgramingLanguageSerializer(ModelSerializer):
    class Meta:
        model = ProgramingLanguageModel
        fields: str = '__all__'

