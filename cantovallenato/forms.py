from crispy_forms.helper import FormHelper
from django import forms
from .models import CantoVallenato, AlbumVallenato, VersionVallenato
from mivalle_core.models.persona import  Persona, Role

class CantoVallenatoForm(forms.ModelForm):
    class Meta:
        model = CantoVallenato
        fields = ['titulo', 'compositor', 'ritmo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input border border-gray-300 rounded-md',}), 
            'compositor': forms.Select(attrs={'placeholder' : 'Compositor', 'class': 'form-input border border-gray-300 rounded-md',}), 
            'ritmo': forms.Select(attrs={'placeholder' : 'Ritmo', 'class': 'form-input border border-gray-300 rounded-md',})}

class FiltroCancionForm(forms.ModelForm):
    compositor = forms.ModelChoiceField(queryset=Persona.objects.filter(roles__name=Role.COMPOSITOR), required=False)

    class Meta:
        model = CantoVallenato
        fields = ['compositor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input border border-gray-300 rounded-md',}), 
            'compositor': forms.TextInput(attrs={'placeholder' : 'Compositor', 'class': 'form-input border border-gray-300 rounded-md',}), 
            'ritmo': forms.TextInput(attrs={'placeholder' : 'Ritmo', 'class': 'form-input border border-gray-300 rounded-md',})}
        
class AbstractPersonaForm(forms.ModelForm):
    """Formulario base para Persona, no se usa directamente."""
    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=False, 
        label='Roles'                                
    )

    class Meta:
        model = Persona     
        fields = '__all__'
        abstract = True   # solo conceptual, no es atributo real de Django        
      
class PersonasPorRolForm(AbstractPersonaForm): 
    """Extiende AbstractPersonaForm para casos específicos."""
    class Meta(AbstractPersonaForm.Meta):
        fields = "__all__"

    def save(self, *args, **kwargs):
        if not self.cleaned_data.get('imagen'):
            raise forms.ValidationError("La imagen es obligatoria.")
        return super().save(*args, **kwargs)

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
        
class AlbumVallenatoForm(forms.ModelForm):
    cancion = forms.ModelChoiceField( queryset=CantoVallenato.objects.all(), required=True, label='Canción', widget=forms.Select(attrs={'class': 'form-control'}) )

    class Meta:
        model = AlbumVallenato
        fields = ['cancion','titulo', 'agrupacion', 'anio_graba', 'isbn']
        labels = {
                    'anio_graba': 'Año'
        } 
        
    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        self.fields['cancion'].label_from_instance = lambda obj: obj.titulo

class VersionVallenatoForm(forms.ModelForm):
    cancion = forms.ModelChoiceField( 
        queryset=CantoVallenato.objects.all(), 
        required=True, label='Canción', 
        widget=forms.Select(attrs={'class': 'form-control'}) 
    )

    class Meta:
        model = VersionVallenato
        fields = ['cancion', 'album', 'interprete']
        widgets = {
            'cancion': forms.Select(attrs={
                'class': 'form-control'
            }),
            'album': forms.Select(attrs={
                'class': 'form-control'
            }),
            'interprete': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
    

class FiltroVersionForm(forms.ModelForm):
    cancion = forms.ModelChoiceField(
        queryset=CantoVallenato.objects.all(), 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = VersionVallenato
        fields = ['cancion']
        widgets = {
            'cancion': forms.TextInput(attrs={
                'class': 'form-control'
            }), 
            'album': forms.TextInput(attrs={
                'placeholder' : 'Album', 
                'class': 'form-control'
            }),
            'agrupacion': forms.TextInput(attrs={
                'placeholder' : 'Agrupacion',
                'class':'form-control'
            })                       
        }

    def __init__(self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        self.fields['cancion'].label_from_instance = lambda obj: obj.titulo
    