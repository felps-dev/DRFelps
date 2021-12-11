from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class LicensedModel(models.Model):
    licenca = models.ForeignKey(
        'core.Licenca',
        on_delete=models.PROTECT,
        default=None,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class User(AbstractUser):
    pass


class Licenca(models.Model):
    cnpj = models.CharField(max_length=14, verbose_name='CNPJ', default=None)


class Pessoa(LicensedModel):
    cpf_cnpj = models.CharField(max_length=14, verbose_name='CNPJ')
    rg_ie = models.CharField(max_length=20, verbose_name='IE / RG')
    razao_social_nome = models.CharField(
        max_length=255, verbose_name='Nome ou Razão Social', default=None)
    nome_fantasia_social = models.CharField(
        max_length=255, verbose_name='Nome Fantasia ou Social', default=None, blank=True, null=True)
    data = models.DateTimeField(
        verbose_name='Data de Cadastro', auto_now_add=True)
    cliente = models.BooleanField(verbose_name='É cliente', default=False)
    funcionario = models.BooleanField(
        verbose_name='É funcionario', default=False)
    fornecedor = models.BooleanField(
        verbose_name='É fornecedor', default=False)
    transportadora = models.BooleanField(
        verbose_name='É transportadora', default=False)
    cep = models.CharField(
        max_length=8, verbose_name='Código de Endereço Postal', default=None, null=True, blank=True)
    endereco = models.CharField(
        max_length=300, verbose_name='Endereço', help_text='Nome da Rua/Endereço', default=None, null=True, blank=True)
    numero = models.CharField(
        max_length=10, verbose_name='Numero', default=None, null=True, blank=True)
    complemento = models.CharField(
        max_length=160, verbose_name='Complemento', default=None, null=True, blank=True)
    uf = models.CharField(max_length=2, verbose_name='UF',
                          help_text='Unidade Federativa', default=None, null=True, blank=True)
    bairro = models.CharField(
        max_length=60, verbose_name='Bairro', default=None, null=True, blank=True)
    cidade = models.CharField(
        max_length=60, verbose_name='Cidade', default=None, null=True, blank=True)
    pais = models.CharField(
        max_length=60, verbose_name='País', default=None, null=True, blank=True)
