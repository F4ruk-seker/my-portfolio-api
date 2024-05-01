from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = "api"

urlpatterns = [
    path('page/', include('pages.api.urls'), name='pages'),
    path('message/', include('message.api.urls'), name='pages'),
    path('auth/', include('custom_auth.api.urls'), name='pages'),
    path('admin/', include('custom_admin.api.urls'), name='custom_admin'),
    path('content/', include('projects.api.urls'), name='project'),
    path('tag/', include('tags.api.urls'), name='tags'),
    path('todo/', include('todo.api.urls'), name='todo'),
    path('game/', include('game.api.urls'), name='game'),
    path('analytical/', include('analytical.api.urls'), name='analytical'),
    path('resume/', include('resume.api.urls'), name='resume'),
]

