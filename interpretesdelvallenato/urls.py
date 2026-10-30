from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from interpretesdelvallenato.views import AgrupacionesView

urlpatterns = [

# Vista de ingreso a la app
path('agrupaciones/', AgrupacionesView.as_view(), name='agrupaciones'),
# Crear agrupación
#path('agrupacion/nueva/', AgrupacionMusicalCreateView.as_view(), name='agrupacionvallenato_create'),
# Listado de agrupaciones (ListView)
#path('agrupaciones/lista/', AgrupacionMusicalListView.as_view(), name='agrupacionesvallenato_list'),
# Detalle, edición y borrado
#path('agrupacion/<int:pk>/', AgrupacionMusicalDetailView.as_view(), name='agrupacionvallenato_detail'),
#path('agrupacion/<int:pk>/edit/', AgrupacionMusicalUpdateView.as_view(), name='agrupacionvallenato_edit'),
#path('agrupacion/<int:pk>/delete/', AgrupacionMusicalDeleteView.as_view(), name='agrupacionvallenato_delete'),
]