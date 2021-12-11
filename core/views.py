from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import Pessoa
from core.serializers import PessoaSerializer
# Create your views here.


class GetClassMixin(object):
    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_action_classes[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_action_classes['default']]

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class LicencedModelViewSet(ModelViewSet):

    def get_queryset(self):
        if(hasattr(self.request.user, 'licenca')):
            return super().get_queryset().filter(licenca=self.request.user.licenca)
        else:
            return super().get_queryset()

    def perform_authentication(self, request):
        if(hasattr(request.user, 'licenca')):
            if(request.method == 'POST' or request.method == 'PATCH' or request.method == 'PUT'):
                request.data['licenca'] = request.user.licenca.id


class PessoaViewSet(LicencedModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    filterset_fields = ('id', 'cpf_cnpj', 'nome_fantasia_social',
                        'rg_ie', 'cliente', 'funcionario', 'fornecedor',
                        'transportadora')
    search_fields = ('id', 'razao_social_nome')
    ordering = ('id')
