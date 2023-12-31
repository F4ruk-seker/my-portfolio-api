from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views


app_name = "pages"


urlpatterns = [
    path('analytics/', views.PagesAnalyticsView.as_view(), name='page-analytics'),
    # path('analytics/<str:name>/', PageView.as_view(), name='page-analytics'),
    path('<str:name>/', views.PageView.as_view(), name='page'),
]


