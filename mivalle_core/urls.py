from django.urls import path
from .views import (
    PersonaCreateView, 
    PersonaUpdateView,
    PersonaDeleteView,     
    PersonasPorRolListView,
    PersonaFiltradaListView,
    PersonaDetailView,
    AgrupacionMusicalCreateView, 
    AgrupacionMusicalUpdateView, 
    AgrupacionMusicalListView, 
    AgrupacionMusicalDetailView, 
    AgrupacionMusicalDeleteView, 
    AgrupacionesView,
)

urlpatterns = [
    # --- Rutas para Persona ---

    # Rutas protegidas
    path("personas/nueva/", PersonaCreateView.as_view(), name="persona_create"),
    path("personas/<int:pk>/editar/", PersonaUpdateView.as_view(), name="persona_edit"),
    path('persona/<int:pk>/', PersonaDetailView.as_view(), name='persona_detail'),
    path("persona/<int:pk>/delete/", PersonaDeleteView.as_view(), name="persona_delete"),
    
    # Rutas públicas
    path("personas/por_rol/", PersonasPorRolListView.as_view(), name="personas_por_rol_list"),
    path("personas/<str:rol>/", PersonasPorRolListView.as_view(), name="personas_por_rol_list"),    
    path("personas/<str:rol>/<str:lugar>/", PersonaFiltradaListView.as_view(), name="personas_por_rol_lugar"),
    

    # --- Rutas para AgrupacionMusical ---
    # Rutas públicas
    # Vista de ingreso a la app
    path('agrupaciones/', AgrupacionesView.as_view(), name='agrupaciones'),

    # Listado de agrupaciones (ListView)
    path("agrupaciones/lista", AgrupacionMusicalListView.as_view(), name="agrupacionesvallenato_list"),

    # Detalle
    path('agrupacion/<int:pk>/', AgrupacionMusicalDetailView.as_view(), name='agrupacionvallenato_detail'),    

    # Rutas protegidas
    # Crear agrupación
    path("agrupacion/nueva/",        
    AgrupacionMusicalCreateView.as_view(), name="agrupacionvallenato_create"),
    # Edición y borrado
    path("agrupaciones/<int:pk>/edit/", 
    AgrupacionMusicalUpdateView.as_view(), name="agrupacionvallenato_edit"),
    path('agrupacion/<int:pk>/delete/', AgrupacionMusicalDeleteView.as_view(), name='agrupacionvallenato_delete'),
]