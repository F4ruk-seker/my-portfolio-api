from rest_framework import serializers
from resume.models import ResumeModel, WorkExperiencesModel, ProjectExperiencesModel
from .work_experiences_serializer import WorkExperiencesSerializer
from .project_experiences_serializer import ProjectExperiencesSerializer
from .contact_serializer import ContactSerializer


class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResumeModel
        exclude: tuple = 'user',


class ResumeEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeModel
        exclude: tuple = 'user',


class ResumeAlpha(serializers.ModelSerializer):
    contact = ContactSerializer(required=False)
    work_experiences = serializers.SerializerMethodField()
    project_experiences = serializers.SerializerMethodField()

    def get_experiences(self, model):
        request = self.context.get('request')
        return model.objects.all() if request.user.is_authenticated else model.objects.filter(show=True)

    def get_project_experiences(self, instance):
        pyload = self.get_experiences(ProjectExperiencesModel)
        return ProjectExperiencesSerializer(instance=pyload, many=True, required=False).data

    def get_work_experiences(self, instance):
        pyload = self.get_experiences(WorkExperiencesModel)
        return WorkExperiencesSerializer(instance=pyload, many=True, required=False).data

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact', None)
        instance = super().update(instance, validated_data)
        if contact_data:
            contact_instance = instance.contact
            for attr, value in contact_data.items():
                setattr(contact_instance, attr, value)
            contact_instance.save()
        return instance

    class Meta:
        model = ResumeModel
        fields: str = '__all__'
        # exclude: tuple = 'id',

