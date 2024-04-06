from django.urls import path
from .views import ResumeView, ResumeRetrieveUpdateDestroyView


app_name = "resume"

urlpatterns = [
    path('edit/<user__username>', ResumeRetrieveUpdateDestroyView.as_view(), name='resume-edit'),
    path('<user__username>', ResumeView.as_view(), name='resume'),
]

