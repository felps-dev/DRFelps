from drf_writable_nested.serializers import WritableNestedModelSerializer
from core.models import Pessoa


class PessoaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
