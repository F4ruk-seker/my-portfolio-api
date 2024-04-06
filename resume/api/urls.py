from django.urls import path
from .views import ResumeView, ResumeRetrieveUpdateDestroyView


app_name = "resume"

urlpatterns = [
    path('edit/', ResumeRetrieveUpdateDestroyView.as_view(), name='resume-edit'),
    path('', ResumeView.as_view(), name='resume'),
]

