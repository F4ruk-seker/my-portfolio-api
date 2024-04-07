from django.urls import path
from .views import *


app_name = "resume"

urlpatterns = [
    path('experience/create', WorkExperiencesCreateView.as_view(), name='experience-create'),
    path('experience/<pk>', WorkExperiencesRetrieveUpdateDestroyView.as_view(), name='experience-edit'),
    path('edit/', ResumeRetrieveUpdateDestroyView.as_view(), name='resume-edit'),
    path('', ResumeView.as_view(), name='resume'),
]

