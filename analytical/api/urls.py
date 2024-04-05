from django.urls import path
from . import views

app_name = "analytical"

urlpatterns = [
    path('ip/<ip>', views.UserFlow.as_view(), name='user_flow'),
    path('content/<pk>', views.ContentTimeTick.as_view(), name='content_time_tick'),
    path('items', views.Items.as_view(), name='items')
    # path('page/', include('pages.api.urls'), name='pages'),
]


