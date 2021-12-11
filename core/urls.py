from django.urls import include, path
from rest_framework import routers
from core.views import *

router = routers.DefaultRouter()
router.register(r'pessoa', PessoaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
