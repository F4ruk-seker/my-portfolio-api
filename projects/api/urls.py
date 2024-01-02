from django.urls import path
from projects.api.views import AllProjectsListView, ProjectRetrieveView


app_name = "project"

urlpatterns = [
    path('all/', AllProjectsListView.as_view(), name='all_projects'),
    path('<str:slug>/', ProjectRetrieveView.as_view(), name='project'),
]
