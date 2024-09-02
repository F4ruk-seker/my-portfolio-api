"""
URL configuration for f4v2cv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from config.settings.base import env
from django.conf.urls.static import static

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'pages', PageView, basename='task')

urlpatterns = [
    # path('', include(router.urls)),
    path('api/', include('api.urls'))
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) if settings.DEBUG else []

if settings.DEBUG:
    import debug_toolbar
    print("*/__debug__/ dahil edildi")
    urlpatterns.append(path('admin/', admin.site.urls))
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
else:
    urlpatterns.append(path(f'{env("ADMIN_PATH")}/', admin.site.urls))
