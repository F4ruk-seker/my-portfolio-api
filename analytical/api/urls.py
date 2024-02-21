from django.urls import path, include
from .views import UserFlow

app_name = "analytical"

urlpatterns = [
    path('ip/<ip>', UserFlow.as_view(), name='user_flow')
    # path('page/', include('pages.api.urls'), name='pages'),
]


