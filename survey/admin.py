from django.contrib import admin
from .models import *

admin.site.register(SurveyUser)
admin.site.register(Survey)
admin.site.register(QuestionPool)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Platform)
