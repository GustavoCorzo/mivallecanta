from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models.query import QuerySet
from django.db.models import Count
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from .models import Promotor, Role
from .forms import PromotoresPorRolForm

class PromotoresView(TemplateView):
     template_name = 'promotoresdelvallenato/promotores/promotores.html'

class PromotorCreateView(CreateView):
    model = Promotor
    form_class = PromotoresPorRolForm
    template_name = 'promotoresdelvallenato/promotores/promotores_por_rol_form.html'

    def get_success_url(self):
        rol = self.object.roles.first().name        
        return reverse_lazy('promotores_por_rol_list', kwargs={'rol':rol})

class PromotoresPorRolListView(ListView):
    model = Promotor
    template_name = 'promotoresdelvallenato/promotores/promotores_por_rol_list.html'
    context_object_name = 'promotores' 
    paginate_by = 15  # Número de promotores por página
    
    def get_queryset(self):        
        rol = self.kwargs.get('rol') 
        return Promotor.objects.filter(roles__name__iexact=rol)
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rol"] = self.kwargs.get('rol')        
        return context

class PromotorDetailView(UpdateView):
    model = Promotor
    form_class = PromotoresPorRolForm
    template_name = 'promotoresdelvallenato/promotores/promotor_detail.html' 
    context_object_name = 'promotor' 
    
    def get_success_url(self):
        return reverse('promotor_detail', kwargs={'pk': self.object.pk})
            
class PromotorUpdateView(UpdateView):
    model = Promotor
    form_class = PromotoresPorRolForm
    template_name = 'promotoresdelvallenato/promotores/actualizapromotor_form.html'
    context_object_name = 'promotor'
    success_url = reverse_lazy('promotores')    

class PromotorDeleteView(DeleteView):
    model = Promotor
    template_name = 'promotoresdelvallenato/promotores/promotor_confirm_delete.html'
    success_url = reverse_lazy('promotores')
