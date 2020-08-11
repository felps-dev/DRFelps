from example.models.contato import Contato
from example.serializers.contato import ContatoSerializer
from rest_framework import viewsets

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    filter_fields = ('id', 'nome')
    search_fields = ('nome')
    ordering = ('nome')
