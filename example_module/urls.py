from django.urls import include, path, re_path
from django.conf.urls import url
from rest_framework import routers
from info.views import *

router = routers.DefaultRouter()
router.register(r'contato', ContatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'somepath/(?P<param>[0-9]{14})/$', get_someurl),
]
