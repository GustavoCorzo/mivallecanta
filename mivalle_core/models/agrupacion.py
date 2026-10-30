from django.db import models
from mivalle_core.models import Persona

class AgrupacionMusical(models.Model):
    razon_social = models.CharField(max_length=150)
    acordeonero = models.ForeignKey('mivalle_core.Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_acordeonero')
    voz_principal = models.ForeignKey('mivalle_core.Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_voz_principal')
    corista_uno = models.ForeignKey('mivalle_core.Persona', on_delete=models.CASCADE, null=True, blank=True, related_name='agrupaciones_corista_uno')
    corista_dos = models.ForeignKey('mivalle_core.Persona', on_delete=models.CASCADE, null=True, blank=True, related_name='agrupaciones_corista_dos')
    cajero = models.ForeignKey('mivalle_core.Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_cajero')
    guacharaquero = models.ForeignKey('mivalle_core.Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_guacharaquero')
    guitarrista = models.ForeignKey('mivalle_core.Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_guitarrista')

    def __str__(self):
        return f'{self.razon_social}'