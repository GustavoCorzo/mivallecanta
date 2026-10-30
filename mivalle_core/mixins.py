from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.views import redirect_to_login
from mivalle_core.templatetags.filters import pluralize_rol, join_roles
from mivalle_core.models import Persona
from mivalle_core.forms import PersonasPorRolForm

class PersonaMixin:
    context_object_name = "persona"
    model = Persona
    form_class = PersonasPorRolForm

    def get_queryset(self):
      """
        Devuelve el conjunto de Personas.
        - Para listados: aplica filtros si hay parámetros en la URL (rol, lugar).
        - Para eliminación: devuelve todos los objetos, así el DeleteView siempre encuentra el objeto.
        """
      qs = Persona.objects.all()

      # Si la vista tiene kwargs de rol o lugar, filtramos
      rol = self.kwargs.get("rol")
      lugar =  self.kwargs.get("lugar")

      if rol:
            qs = qs.filter(rol=rol)
      if lugar:
            qs = qs.filter(lugar=lugar)

      return qs
    
class AgrupacionMusicalMixin:
    context_object_name = "agrupacion"
    model= None    
    
    @property
    def form_class(self):
        from mivalle_core.forms import AgrupacionMusicalForm
        return AgrupacionMusicalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadimos contexto común para todas las vistas que usen este mixin
        context["titulo_seccion"] = "Agrupaciones musicales"
        return context
    
    
            
    