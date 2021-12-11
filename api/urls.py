"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.authtoken.views import ObtainAuthToken
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', ObtainAuthToken.as_view()),
    # YOUR PATTERNS
    path('api/docs/', SpectacularAPIView.as_view(), name='docs'),
    # Optional UI:
    path('api/docs/swui/',
         SpectacularSwaggerView.as_view(url_name='docs'), name='swagger-ui'),
    path('api/docs/redoc/',
         SpectacularRedocView.as_view(url_name='docs'), name='redoc'),
    path('api/', include('core.urls')),
]
