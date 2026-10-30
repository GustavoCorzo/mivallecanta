from django.contrib import admin
from .models import CantoVallenato,  RitmoVallenato, VersionVallenato, AlbumVallenato

@admin.register(RitmoVallenato)
class RitmoVallenataAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(CantoVallenato)
class CantoVallenatoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'compositor', 'ritmo',)

@admin.register(AlbumVallenato)
class AlbumVallenatoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'agrupacion', 'anio_graba', 'isbn',)

@admin.register(VersionVallenato)
class VersionVallenatoAdmin(admin.ModelAdmin):
    list_display = ('cancion', 'album',)
