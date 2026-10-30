#from django.db.models.query import QuerySet
#from django.db.models import Count
#from django.shortcuts import render, get_object_or_404, redirect
#from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView, TemplateView
#from mivalle_core.mixins import AgrupacionMusicalMixin

# Create your views here.

class AgrupacionesView(TemplateView):
     template_name = 'interpretesdelvallenato/interpretes/agrupaciones.html'

#class AgrupacionMusicalUpdateView(AgrupacionMusicalMixin, UpdateView):
    #template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_form.html'
    #success_url = reverse_lazy('agrupacionesvallenato_list')

#class AgrupacionMusicalListView(AgrupacionMusicalMixin, ListView):    
    #template_name = 'cantovallenato/agrupaciones/agrupacionesvallenato_list.html'
    #context_object_name = 'agrupaciones' 
    #paginate_by = 15

#class AgrupacionMusicalDeleteView(AgrupacionMusicalMixin, DeleteView):    
    #template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_confirm_delete.html'
    #success_url = reverse_lazy('agrupacionesvallenato_list')

#class AgrupacionMusicalDetailView(AgrupacionMusicalMixin, DetailView):
    #template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_detail.html'
    #context_object_name = 'agrupacion'

#class AgrupacionMusicalCreateView(AgrupacionMusicalMixin, CreateView):       
    #template_name = 'cantovallenato/agrupaciones/agrupacionvallenato_form.html'
    #success_url = reverse_lazy('agrupacionesvallenato_list')