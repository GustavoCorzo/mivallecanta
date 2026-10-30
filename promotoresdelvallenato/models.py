from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from PIL import Image
import uuid

# Create your models here.
class Role(models.Model): 
    ESCRITOR = 'escritor' 
    JUGLAR = 'juglar' 
    MECENAS = 'mecenas' 
    COLABORADOR = 'colaborador'  
    
    ROLE_CHOICES = [ 
        (ESCRITOR, 'Escritor'), 
        (JUGLAR, 'Juglar'), 
        (MECENAS, 'Mecenas'),         
        (COLABORADOR, 'Colaborador'),
    ]

    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Promotor(models.Model):
    
    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)      
    nombre_apodo_seudonimo = models.CharField(max_length=100)    
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    roles = models.ManyToManyField(Role, blank=True)
    aporte = models.TextField(blank=True, null=True)
   
    class Meta:
        ordering = ["apellidos"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagen and hasattr(self.imagen, 'path'):
            img = Image.open(self.imagen.path)
            max_size = (200, 200)
            img.thumbnail(max_size, Image.LANCZOS)
            img.save(self.imagen.path)    

    def __str__(self):
        return f"{self.nombre_apodo_seudonimo}"