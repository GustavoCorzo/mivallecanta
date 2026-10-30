from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field
from django import forms
from .models import Role, Promotor
from django.shortcuts import render, redirect


class AbstractPromotorForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=True, 
        label='Roles'                                
    )

    class Meta:
        model = Promotor     
        fields = '__all__'

class PromotoresPorRolForm(forms.ModelForm): 
    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'space-y-2'}),
        required=False,
        label='Roles'
    )

    class Meta(AbstractPromotorForm.Meta):        
        model = Promotor
        fields = ['nombres', 'apellidos',  'nombre_apodo_seudonimo', 'imagen', 'roles', 'aporte']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'block w-full rounded-md border-gray-300 shadow-sm'}),
            'apellidos': forms.TextInput(attrs={'class': 'block w-full rounded-md border-gray-300 shadow-sm'}),
            'nombre_apodo_seudonimo': forms.TextInput(attrs={'class': 'block w-full rounded-md border-gray-300 shadow-sm'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'block w-full text-sm text-gray-500'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.layout = Layout(
            Div(
                Field('nombres'),
                Field('apellidos'),
                Field('nombre_apodo_seudonimo'),
                Field('imagen', 'aporte'),
                Div(
                    Field('roles', css_class='mt-4'),                       
                    Submit('submit', 'Guardar', css_class='bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded'),
                    css_class='space-y-4'
            ),
        )
    )

   
    def save(self, commit=True):
        self.instance = super().save(commit=False)
        if commit:
            self.instance.save()
            self.save_m2m()  # Guarda las relaciones ManyToMany después de guardar el promotor
        return self.instance
   