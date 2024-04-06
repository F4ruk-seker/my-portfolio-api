from rest_framework import serializers
from resume.models import ResumeModel, ContactModel
import markdown_to_json


class ResumeSerializer(serializers.ModelSerializer):
    # context = serializers.SerializerMethodField(read_only=True)
    #
    # @staticmethod
    # def get_context(instance):
    #     return markdown_to_json.dictify(instance.context)

    class Meta:
        model = ResumeModel
        exclude: tuple = 'user',


class ResumeEditSerializer(serializers.ModelSerializer):
    # marked = serializers.SerializerMethodField(read_only=True, required=False)
    #
    # @staticmethod
    # def get_marked(instance):
    #     return markdown_to_json.dictify(instance.context)

    class Meta:
        model = ResumeModel
        exclude: tuple = 'user',


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        # fields: str = '__all__'
        exclude: tuple = 'id',


class ResumeAlpha(serializers.ModelSerializer):
    contact = ContactSerializer(required=False)

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact', None)
        instance = super().update(instance, validated_data)
        if contact_data:
            print(contact_data)
            contact_instance = instance.contact
            for attr, value in contact_data.items():
                setattr(contact_instance, attr, value)
            contact_instance.save()
        return instance

    class Meta:
        model = ResumeModel
        fields: str = '__all__'
        # exclude: tuple = 'id',

