from django.contrib import admin
from .models import ResumeModel, ContactModel, WorkExperiencesModel, ProjectExperiencesModel


admin.site.register(ResumeModel)
admin.site.register(ContactModel)
admin.site.register(WorkExperiencesModel)
admin.site.register(ProjectExperiencesModel)

