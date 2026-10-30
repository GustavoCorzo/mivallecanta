from django.db.models.query import QuerySet
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from mivalle_core.models.agrupacion import AgrupacionMusical
from mivalle_core.views import PersonaFiltradaListView
from mivalle_core.models.persona import  Persona, Role
from .models import CantoVallenato, AlbumVallenato, VersionVallenato
from .forms import CantoVallenatoForm, FiltroCancionForm, AlbumVallenatoForm, VersionVallenatoForm, FiltroVersionForm, PersonasPorRolForm, PersonaFiltroForm
from mivalle_core.forms import AgrupacionMusicalForm 

# 📜 Vista basada en función para listado personalizado
def listado_personas(request):
        lugar = request.GET.get('lugar', 'Todos')
        rol = request.GET.get('rol', 'compositor')

        # Obtener el objeto Role correspondiente
        try:
            rol_obj = Role.objects.get(name=rol)
        except Role.DoesNotExist:
            rol_obj = None

        # Filtrar personas según rol y lugar
        if rol_obj:
            if lugar != 'Todos':
                personas = Persona.objects.filter(roles__name=rol, lugar_nace=lugar)
            else:
                personas = Persona.objects.filter(roles=rol_obj)
        else:
            personas = Persona.objects.none()    
         
        
        context = {
            'personas': personas,
            'rol': rol_obj.name if rol_obj else rol, 
            'rol_plural': PersonaFiltradaListView.pluralize_rol(rol_obj.get_name_display()) if rol_obj else rol,            
            'lugar': None if lugar == 'Todos' else lugar,
        }
        return render (request, 'personas_por_rol_lugar.html', context)

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class CantaresView(TemplateView):
     template_name = 'cantovallenato/canciones/cantarvallenato.html'

class AgrupacionesView(TemplateView):
     template_name = 'cantovallenato/agrupaciones/agrupacionesvallenato.html'

class CreadoresView(TemplateView):
     template_name = 'cantovallenato/creadores/creadoresdelvallenato.html'

class RitmosView(TemplateView):
     template_name = 'cantovallenato/ritmos/ritmosdelvallenato.html'

class InstrumentosView(TemplateView):
     template_name = 'cantovallenato/instrumentos/instrumentosdelvallenato.html'

class CantoVallenatoCreateView(CreateView):
    model = CantoVallenato
    form_class = CantoVallenatoForm    
    template_name = 'cantovallenato/canciones/cantovallenato_form.html'
    context_object_name = 'canto'
    success_url = reverse_lazy('cantovallenato_list')

class CantoVallenatoListView(ListView):
    model = CantoVallenato
    template_name = 'cantovallenato/canciones/cantovallenato_list.html'
    context_object_name = 'cantos'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        compositor_id = self.request.GET.get('compositor')
        if compositor_id:
            queryset = queryset.filter(compositor_id=compositor_id)
        return queryset         
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FiltroCancionForm(self.request.GET or None)
        return context    
    
class CantoVallenatoUpdateView(UpdateView):
    model = CantoVallenato
    form_class = CantoVallenatoForm
    template_name = 'cantovallenato/canciones/actualizacanto_form.html'
    success_url = reverse_lazy('cantovallenato_list')

class CantoVallenatoDeleteView(DeleteView):
    model = CantoVallenato
    template_name = 'cantovallenato/canciones/cantovallenato_confirm_delete.html'
    success_url = reverse_lazy('cantovallenato_list')

#class PersonaCreateView(CreateView):
    #model = Persona
    #form_class = PersonasPorRolForm
    #template_name = 'cantovallenato/creadores/personas_por_rol_form.html'

    #def get_success_url(self):
        #rol = self.object.roles.first().name
        #return reverse_lazy('personas_por_rol_lugar', kwargs={'rol':rol,  'lugar': 'todos'})

#class PersonaPorRolListView(ListView):
    #model = Persona
    #template_name = 'cantovallenato/creadores/#personas_por_rol_list.html'
    #context_object_name = 'personas' 
    #paginate_by = 15  # Número de personas por página
    
    #def get_queryset(self):        
        #rol = self.kwargs.get('rol')
        #lugar_url = self.kwargs.get('lugar')
        #lugar_query = self.request.GET.get('lugar')
        

        #queryset = super().get_queryset()

        #if rol:
           #queryset = queryset.filter(roles__name__iexact=rol)

        #lugar_final = lugar_query or lugar_url
        #if lugar_final and lugar_final.lower() != 'todos':
            #queryset = queryset.filter(lugar_nace__icontains=lugar_final) 

        #return queryset
    
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #rol = self.kwargs.get('rol')
        
        # Extraer lugares únicos solo para personas con ese rol
        #lugares_disponibles = Persona.objects.filter#(roles__name__iexact=rol).values_list#('lugar_nace', flat=True).distinct().order_by#('lugar_nace')        
        #context['lugares_disponibles'] = [lugar for #lugar in lugares_disponibles if lugar]
        #context['rol'] = rol
        #context['lugar'] = self.kwargs.get('lugar') 
        #return context

 # 🎭 Vista basada en clase para paginar y filtrar personas        
#class PersonaFiltradaListView(ListView):
    #model = Persona
    #template_name = 'cantovallenato/creadores/#personas_por_rol_list.html'
    #context_object_name = 'personas'
    #paginate_by = 15 # Número de personas por página

    #def get_queryset(self):
        #rol = self.kwargs.get('rol')        
        #lugar_url = self.kwargs.get('lugar') # Desde la URL
        #lugar_query = self.request.GET.get('lugar') # Desde query string

        #queryset = super().get_queryset()

        #if rol:
            #queryset = queryset.filter(roles__name__iexact=rol)

        # Prioriza el query string si existe
        #lugar_final = lugar_query or lugar_url
        #if lugar_final and lugar_final.lower() != 'todos':
            #queryset = queryset.filter(lugar_nace__iexact=lugar_final)
        
        #return queryset
    
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #rol = self.kwargs.get('rol')
        #lugar_url = self.kwargs.get('lugar')
        #lugar_query = self.request.GET.get('lugar')
        #lugar_final = lugar_query or lugar_url

        #lugares_disponibles = Persona.objects.filter(
            #roles__name__iexact=rol
        #).values_list('lugar_nace', flat=True).distinct().order_by('lugar_nace')
        
        #context.update({
            #'lugares_disponibles': [lugar for lugar in lugares_disponibles if lugar],
            #'rol' : rol,
            #'lugar': lugar_final.capitalize() if lugar_final else 'Todos',
        #})

        #return context

#class PersonaDetailView(DetailView):
    #model = Persona
    #template_name = 'cantovallenato/creadores/#persona_detail.html' 
    #context_object_name = 'persona' 
            
#class PersonaUpdateView(UpdateView):
    #model = Persona
    #form_class = PersonasPorRolForm
    #template_name = 'cantovallenato/creadores/#actualizacreador_form.html'
    #success_url = reverse_lazy('cantarvallenato')
    #def form_valid(self, form):
        #if 'imagen' in form.changed_data:
            #return super().form_valid(form)
        #else:
            #form.instance.imagen = self.object.imagen
        #return super().form_valid(form)

#class PersonaDeleteView(DeleteView):
    #model = Persona
    #template_name = 'cantovallenato/creadores/#creador_confirm_delete.html'
    #success_url = reverse_lazy('cantarvallenato')

#class AgrupacionMusicalCreateView(CreateView):
    #model = AgrupacionMusical
    #form_class = AgrupacionMusicalForm    
    #template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_form.html'
    #success_url = reverse_lazy('agrupacionesvallenato_list')

#class AgrupacionMusicalListView(ListView):
    #model = AgrupacionMusical
    #template_name = 'cantovallenato/agrupaciones/agrupacionesvallenato_list.html'
    #context_object_name = 'agrupaciones' 
    #paginate_by = 15   

#class AgrupacionMusicalDetailView(DetailView):
    #model = AgrupacionMusical
    #template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_detail.html'
    #context_object_name = 'agrupacion'

#class AgrupacionMusicalUpdateView(UpdateView):
    #model = AgrupacionMusical
    #form_class = AgrupacionMusicalForm
    #template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_form.html'
    #success_url = reverse_lazy('agrupacionesvallenato_list')

#class AgrupacionMusicalDeleteView(DeleteView):
    #model = AgrupacionMusical
    #template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_confirm_delete.html'
    #success_url = reverse_lazy('agrupacionesvallenato_list')

class AlbumVallenatoCreateView(CreateView):
    model = AlbumVallenato
    form_class = AlbumVallenatoForm    
    template_name = 'cantovallenato/albumes/albumvallenato_form.html'
    success_url = reverse_lazy('albumesvallenato_list')

class AlbumVallenatoListView(ListView):
    model = AlbumVallenato
    template_name = 'cantovallenato/albumes/albumesvallenato_list.html'
    context_object_name = 'albumes' 
    paginate_by = 15   

class AlbumVallenatoDetailView(DetailView):
    model = AlbumVallenato
    template_name = 'cantovallenato/albumes/albumvallenato_detail.html'
    context_object_name = 'album'

class AlbumVallenatoUpdateView(UpdateView):
    model = AlbumVallenato
    form_class = AlbumVallenatoForm 
    template_name = 'cantovallenato/albumes/actualizalbum_form.html'
    success_url = reverse_lazy('albumesvallenato_list')

class AlbumVallenatoDeleteView(DeleteView):
    model = AlbumVallenato
    template_name = 'cantovallenato/albumes/albumvallenato_confirm_delete.html'
    success_url = reverse_lazy('albumesvallenato_list')


class VersionVallenatoCreateView(CreateView):
    model = VersionVallenato
    form_class = VersionVallenatoForm    
    template_name = 'cantovallenato/versiones/versionvallenato_form.html'
    success_url = reverse_lazy('versionesvallenato_list')

class VersionVallenatoListView(ListView):
    model = VersionVallenato
    template_name = 'cantovallenato/versiones/versionesvallenato_list.html'
    context_object_name = 'versiones'
    paginate_by = 15 

    def get_queryset(self):
        queryset = super().get_queryset()
        cancion = self.request.GET.get('cancion')
        if cancion:
            queryset = queryset.filter (cancion__id=cancion)
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = FiltroVersionForm(self.request.GET or None)   # aquí sí defines form
        context['form'] = form
        if form.is_valid():
            context['cancion'] = form.cleaned_data.get('cancion')
        return context

class VersionVallenatoDetailView(DetailView):
    model = VersionVallenato
    template_name = 'cantovallenato/versiones/versionvallenato_detail.html'
    context_object_name = 'version'

class VersionVallenatoUpdateView(UpdateView):
    model = VersionVallenato
    form_class = VersionVallenatoForm
    template_name = 'cantovallenato/versiones/versionvallenato_form.html'
    success_url = reverse_lazy('versionesvallenato_list')

class VersionVallenatoDeleteView(DeleteView):
    model = VersionVallenato
    template_name = 'cantovallenato/versiones/versionvallenato_confirm_delete.html'
    success_url = reverse_lazy('versionesvallenato_list')