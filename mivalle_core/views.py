from django.urls import reverse_lazy
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
import traceback
from mivalle_core.models import AgrupacionMusical, Persona, Role
from django.contrib.auth.mixins import LoginRequiredMixin
from mivalle_core.forms import PersonaForm, PersonasPorRolForm, AgrupacionMusicalForm
from django.views.generic import CreateView, UpdateView, DeleteView
from .mixins import PersonaMixin, AgrupacionMusicalMixin

from django.urls import reverse

# --- Vistas para Persona ---
class PersonaCreateView(PersonaMixin, CreateView):    
    model = Persona
    form_class = PersonasPorRolForm
    template_name = 'cantovallenato/creadores/personas_por_rol_form.html'
    success_url = reverse_lazy('personas_por_rol_list')

    def get_success_url(self):
        first_role = self.object.roles.first()
        rol = first_role.name if first_role else "compositor" # rol por defecto
        return reverse_lazy('personas_por_rol_lugar', kwargs={'rol':rol,  'lugar': 'todos'})

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            self.object.roles.set(form.cleaned_data['roles'])  # 🔑 guardar roles
            messages.success(self.request, "El creador fue registrado correctamente")
            return response
        
        except IntegrityError:
            form.add_error('nombre_artistico', "Este creador ya existe.")       
            messages.error(self.request, "No se puede registrar: el creador ya existe.")
            return self.form_invalid(form)

        print(form.cleaned_data)
    
class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'cantovallenato/creadores/persona_detail.html' 
    context_object_name = 'persona'    
        
class PersonaUpdateView(PersonaMixin, UpdateView):    
    template_name = 'cantovallenato/creadores/actualizacreador_form.html'
    success_url = reverse_lazy('personas_por_rol_list')

    def form_valid(self, form):
        # Si no se sube nueva imagen, conservar la existente
        if not form.cleaned_data.get('imagen'):
            form.instance.imagen = self.object.imagen
        return super().form_valid(form)

class PersonaDeleteView(PersonaMixin, DeleteView ): 
    model = Persona   
    template_name = 'cantovallenato/creadores/creador_confirm_delete.html'
    success_url = reverse_lazy("personas_por_rol_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        nombre = getattr(self.object, "nombre_artistico", str(self.object))
        messages.success(request, f'El creador "{nombre}" fue eliminado correctamente.')
        return super().delete(request, *args, **kwargs)              

class PersonasPorRolListView(PersonaMixin, ListView):
    model = Persona
    template_name = 'cantovallenato/creadores/personas_por_rol_list.html'
    context_object_name = 'personas' 
    paginate_by = 15  # Número de personas por página
    
    def get_queryset(self):
        queryset = super().get_queryset()

        rol = self.kwargs.get('rol', None)
        if rol:
           queryset = queryset.filter(roles__name__iexact=rol)

        lugar_query = self.request.GET.get("lugar", None)
        lugar_url = self.kwargs.get('lugar', None)
        lugar_final = self.request.GET.get("lugar") or self.kwargs.get("lugar")

        if lugar_final and lugar_final.lower() != 'todos':
            queryset = queryset.filter(lugar_nace__icontains=lugar_final) 

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rol = self.kwargs.get('rol', None)
        lugar_query = self.request.GET.get("lugar", None)
        lugar_url = self.kwargs.get("lugar", None)
        lugar_final = lugar_query or lugar_url or "todos"
        
        # Extraer lugares únicos solo para personas con ese rol
        lugares_disponibles = Persona.objects.filter(roles__name__iexact=rol).values_list('lugar_nace', flat=True).distinct().order_by('lugar_nace')        
        context['lugares_disponibles'] = [lugar for lugar in lugares_disponibles if lugar]

        # valores para el template
        context['rol'] = rol or "creador"
        context['lugar'] = lugar_final
        context['lugares_disponibles'] = Persona.objects.values_list("lugar_nace", flat=True).distinct
        return context
    
#Vista basada en clase para paginar y filtrar personas        
class PersonaFiltradaListView(ListView):
    model = Persona
    template_name = 'cantovallenato/creadores/personas_por_rol_list.html'
    context_object_name = 'personas'
    paginate_by = 15 # Número de personas por página

    def get_queryset(self):
        rol = self.kwargs.get('rol')        
        lugar_url = self.kwargs.get('lugar') # Desde la URL
        lugar_query = self.request.GET.get('lugar') # Desde query string

        queryset = super().get_queryset()

        if rol:
            queryset = queryset.filter(roles__name__iexact=rol)

         #Prioriza el query string si existe
        lugar_final = lugar_query or lugar_url
        if lugar_final and lugar_final.lower() != 'todos':
            queryset = queryset.filter(lugar_nace__iexact=lugar_final)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rol = self.kwargs.get('rol')
        lugar_url = self.kwargs.get('lugar')
        lugar_query = self.request.GET.get('lugar')
        lugar_final = lugar_query or lugar_url

        lugares_disponibles = Persona.objects.filter(
            #roles__name__iexact=rol
        ).values_list('lugar_nace', flat=True).distinct().order_by('lugar_nace')
        
        context.update({
            'lugares_disponibles': [lugar for lugar in lugares_disponibles if lugar],
            'rol' : rol,
            'lugar': lugar_final.capitalize() if lugar_final else 'Todos',
        })

        return context
    
# --- Vistas para AgrupacionMusical ---
# --- Vistas públicas ---
class AgrupacionesView(TemplateView):
     template_name = 'interpretesdelvallenato/interpretes/agrupaciones.html'

class AgrupacionMusicalListView(AgrupacionMusicalMixin, ListView):
    model = AgrupacionMusical
    template_name = "cantovallenato/agrupaciones/agrupacionesvallenato_list.html"
    context_object_name = "agrupaciones"
    paginate_by = 15

class AgrupacionMusicalDetailView(AgrupacionMusicalMixin, DetailView):
    model = AgrupacionMusical
    template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_detail.html'
    context_object_name = 'agrupacion'

# --- Vistas protegidas ---
class AgrupacionMusicalCreateView(AgrupacionMusicalMixin, CreateView):
    model = AgrupacionMusical
    form_class = AgrupacionMusicalForm
    template_name = "cantovallenato/agrupaciones/agrupacionvallenato_form.html"
    success_url = reverse_lazy("agrupacionesvallenato_list")
    login_url = "/accounts/login"    # URL de login
    redirect_field_name = "next"     # parámetro de redirección


class AgrupacionMusicalUpdateView(AgrupacionMusicalMixin, UpdateView):
    model = AgrupacionMusical
    form_class = AgrupacionMusicalForm
    template_name = "cantovallenato/agrupaciones/actualizagrupacion_form.html"
    success_url = reverse_lazy('agrupacionesvallenato_list')

class AgrupacionMusicalDeleteView(AgrupacionMusicalMixin, DeleteView):
    model = AgrupacionMusical    
    template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_confirm_delete.html'
    success_url = reverse_lazy('agrupacionesvallenato_list')




