from django.urls import path
from django.db.models.query import QuerySet
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from .models import Promotor, Role
from .forms import AbstractPromotorForm, PromotoresPorRolForm
from promotoresdelvallenato.views import PromotoresView, PromotorCreateView, PromotoresPorRolListView, PromotorDetailView, PromotorUpdateView, PromotorDeleteView

urlpatterns = [
    path('promotores/', PromotoresView.as_view(), name='promotores'),
    path('promotor/nuevo', PromotorCreateView.as_view(), name='crear_promotor'),
    path('promotores/<str:rol>/', PromotoresPorRolListView.as_view(), name='promotores_por_rol_list'),
    # Vista de detalle
    path('promotor/<int:pk>/', PromotorDetailView.as_view(), name='promotor_detail'),
    # Vista de edición
    path("promotor/<int:pk>/edit", PromotorUpdateView.as_view(), name="promotor_edit"),
    path("promotor/<int:pk>/delete", PromotorDeleteView.as_view(), name="promotor_delete"),
  
]