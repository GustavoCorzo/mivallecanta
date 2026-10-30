from django.contrib import admin
from mivalle_core.models import Persona, AgrupacionMusical, Role

# Register your models here.
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre_artistico',)

@admin.register(AgrupacionMusical)
class AgrupacionMusicalAdmin(admin.ModelAdmin):
    list_display = ('razon_social',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

