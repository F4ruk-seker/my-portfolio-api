from django.urls import path, include
from tags.api import views


app_name = "tags"

urlpatterns = [
    path('all/', views.AllTagsListView.as_view(), name='project'),
]


