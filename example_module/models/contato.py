from django.db import models
from core.models.licensemodel import LicenseModel


class Contato(LicenseModel):
    nome = models.CharField(
        verbose_name="Telefone", max_length=80, default=None, null=True, blank=True)
    email = models.EmailField(verbose_name='E-Mail',
                              default=None, null=True, blank=True)
    telefone = models.CharField(
        verbose_name="Telefone", max_length=20, default=None, null=True, blank=True)
