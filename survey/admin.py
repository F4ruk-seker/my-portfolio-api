from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin


admin.site.register(SurveyUser, ModelAdmin)
admin.site.register(Survey, ModelAdmin)
admin.site.register(QuestionPool, ModelAdmin)
admin.site.register(Question, ModelAdmin)
admin.site.register(Response, ModelAdmin)
admin.site.register(Platform, ModelAdmin)
