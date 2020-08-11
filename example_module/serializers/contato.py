from rest_framework import serializers
from example.models.contato import Contato


class ContatoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = Contato
        fields = (
            'id',
            'nome',
            'email',
            'telefone',
        )
