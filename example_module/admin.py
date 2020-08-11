from django.contrib import admin
from info.models.contato import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)
