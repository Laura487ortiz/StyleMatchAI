from django.contrib import admin
from .models import FotoArmario

@admin.register(FotoArmario)
class FotoArmarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen', 'vector_caracteristicas')
