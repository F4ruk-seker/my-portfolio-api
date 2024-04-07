from resume.models import ContactModel
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        # fields: str = '__all__'
        exclude: tuple = 'id',
