from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import InlineCheckboxes
from mivalle_core.models.agrupacion import AgrupacionMusical
from mivalle_core.models.persona import  Persona, Role

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class AbstractPersonaForm(forms.ModelForm):
    """Formulario base para Persona, no se usa directamente."""
    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=True, 
        label='Roles'                                
    )

    class Meta:
        model = Persona
        fields = '__all__'                      
          
class PersonasPorRolForm(forms.ModelForm):     
    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(),        
        required=False, 
        label='Roles' 
                                        
    )
    class Meta:
        model = Persona 
        fields = [
            'nombres', 'apellidos', 'formacion_academica', 'nombre_artistico',
            'anio_nace', 'lugar_nace', 'lugar_muere', 'imagen', 'roles'
            ]
        widgets = {
            'roles': forms.CheckboxSelectMultiple(attrs={'class': 'hidden peer'})
        }
        labels = {
                    'anio_nace': 'Año nacimiento'
        }  
        
    def clean_nombre_artistico(self):
        nombre = self.cleaned_data['nombre_artistico']
        # Permitir el mismo valor si es el mismo objeto        
        if Persona.objects.filter(nombre_artistico=nombre).exclude(pk=self.instance.pk).exists():   
            raise forms.ValidationError("Ese nombre artístico ya está registrado")
        return nombre
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)         
        
        # eliminar cualquier campo 'roles' que venga del modelo
        if 'roles' in self.fields:
            del self.fields['roles']

        # volver a registrar el campo manual
        self.fields['roles'] = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'space-y-2'}),
        required=False,
        label='Roles'
    ) 
        # Configuración de crispy
        self.helper = FormHelper() 
        self.helper.form_method = "post"
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.form_class = 'space-y-4' # 🔑 aquí aplicas clase al <form>
        self.helper.layout = Layout(
            Field("nombres"),
            Field("apellidos"),
            Field("formacion_academica"),  # respeta el widget Select
            Field("nombre_artistico"),
            Field("anio_nace"),
            Field("lugar_nace"),
            Field("lugar_muere"),
            Field("imagen"),
            InlineCheckboxes("roles", css_class="grid grid-cols-1 sm:grid-cols-2 gap-4"),   
            # respeta el widget CheckboxSelectMultiple
            Submit("submit", "Guardar",
                    css_class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
            )            
        )      

class PersonaFiltroForm(forms.Form):
    """Formulario simple para filtrar personas en vistas/listados."""
    lugar_nace = forms.CharField(
        label="Lugar de nacimiento",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-input mt-1 block w-full",
            "placeholder": "Ej. Valledupar"
        })
    )
        
class AgrupacionMusicalForm(forms.ModelForm):
    class Meta:
        model = AgrupacionMusical
        fields = ['razon_social', 'acordeonero', 'voz_principal', 'corista_uno', 'corista_dos', 'cajero', 'guacharaquero', 'guitarrista']
