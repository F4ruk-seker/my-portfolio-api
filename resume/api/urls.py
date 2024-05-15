from django.urls import path
from .views import *


app_name = "resume"

urlpatterns = [
    path('experience/create', WorkExperiencesCreateView.as_view(), name='experience-create'),
    path('experience/<pk>', WorkExperiencesRetrieveUpdateDestroyView.as_view(), name='experience-edit'),
    path('project/create', ProjectExperiencesCreateView.as_view(), name='project-create'),
    path('project/<pk>', ProjectExperiencesRetrieveUpdateDestroyView.as_view(), name='project-edit'),
    path('edit/', ResumeRetrieveUpdateDestroyView.as_view(), name='resume-edit'),
    path('', ResumeView.as_view(), name='resume'),
]

