from django.contrib import admin
from .models import Promotor, Role

# Register your models here.
@admin.register(Promotor)
class PromotorAdmin(admin.ModelAdmin):
    list_display = ('nombre_apodo_seudonimo', )

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)