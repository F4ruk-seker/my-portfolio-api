from django.contrib import admin
from .models import ResumeModel, ContactModel, WorkExperiencesModel, ProjectExperiencesModel
from unfold.admin import ModelAdmin


admin.site.register(ResumeModel, ModelAdmin)
admin.site.register(ContactModel, ModelAdmin)
admin.site.register(WorkExperiencesModel, ModelAdmin)
admin.site.register(ProjectExperiencesModel, ModelAdmin)

