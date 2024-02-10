from django.urls import path
from projects.api.views import (ContentFlagsView,
                                AllProjectsListView,
                                ProjectRetrieveView,
                                ProjectRetrieveUpdateDestroyView,
                                CreateCommentView)


app_name = "project"
urlpatterns = [
    path('type/<name>', ContentFlagsView.as_view(), name='content_flags'),
    path('all/', AllProjectsListView.as_view(), name='all_projects'),
    # path('create/', ProjectRetrieveUpdateDestroyView.as_view(), name='project'),
    path('edit/<str:slug>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project'),
    path('comment/<str:slug>/', CreateCommentView.as_view(), name='comment'),
    path('<str:slug>/', ProjectRetrieveView.as_view(), name='project'),
]

