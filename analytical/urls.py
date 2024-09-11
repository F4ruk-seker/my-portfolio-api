from django.urls import path
from .views import AnalyticalMediaRedirectView


app_name = "analytical"

urlpatterns = [
    path('media/<slug>', AnalyticalMediaRedirectView.as_view(),),
]

