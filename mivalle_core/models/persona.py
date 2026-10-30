from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from PIL import Image
import uuid

class Role(models.Model): 
    COMPOSITOR = 'compositor' 
    ACORDEONERO = 'acordeonero' 
    CANTANTE = 'cantante'
    CORISTA = 'corista'
    CAJERO = 'cajero'
    GUACHARAQUERO = 'guacharaquero'
    GUITARRISTA = 'guitarrista'
    
    ROLE_CHOICES = [ 
        (COMPOSITOR, 'Compositor'), 
        (ACORDEONERO, 'Acordeonero'), 
        (CANTANTE, 'Cantante'), 
        (CORISTA, 'Corista'),
        (CAJERO, 'Cajero'),
        (GUACHARAQUERO, 'Guacharaquero'),
        (GUITARRISTA, 'Guitarrista'),
    ]

    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class Persona(models.Model):
    NINGUNO = "0"
    PRIMARIA = "1"
    SECUNDARIA = "2"
    PREGRADO = "3"
    POSGRADO = "4"
    FORMACION_ACADEMICA_CHOICES = [
        (NINGUNO, "Ninguno"),
        (PRIMARIA, "Primaria"),
        (SECUNDARIA, "Secundaria"),
        (PREGRADO, "Pregrado"),
        (POSGRADO, "Posgrado"),
    ]

    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    formacion_academica = models.CharField(
        max_length=1,
        choices=FORMACION_ACADEMICA_CHOICES,
        default=PRIMARIA,
    )
    
    nombre_artistico = models.CharField(max_length=100, unique=True)
    anio_nace = models.IntegerField(null=True, blank=True)
    lugar_nace = models.CharField(max_length=50, null=True, blank=True)
    lugar_muere = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    roles = models.ManyToManyField(Role, related_name="personas", blank=True)
   
    class Meta:
        ordering = ["apellidos"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagen and hasattr(self.imagen, 'path'):
            img = Image.open(self.imagen.path)
            max_size = (200, 200)
            img.thumbnail(max_size, Image.LANCZOS)
            img.save(self.imagen.path)

    def get_formacion_academica_display(self):
        return dict(self.FORMACION_ACADEMICA_CHOICES).get(self.formacion_academica, "Desconocido")

    def __str__(self):
        return f"{self.nombre_artistico}"