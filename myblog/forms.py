from django import forms
from .models import Post, Categorias


#elegir = [('EEUU', 'EEUU'), ('Argentina', 'Argentina'), ('España', 'España')]
elegir = Categorias.objects.all().values_list('name', 'name')
elegir_lista = []

for item in elegir:
    elegir_lista.append(item)
class FormArticulo(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag','autor','categorias', 'cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un título para su artículo'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control','value':'','id':'usuario','type':'hidden'}),
            #'autor': forms.Select(attrs={'class': 'form-control', 'value':'','id':'usuario', 'type':'hidden'}),
            'categorias': forms.Select(choices = elegir_lista, attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),

        }

class EditarArticulo(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'cuerpo', 'categorias')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un título para su artículo'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'categorias': forms.Select(choices = elegir_lista, attrs={'class': 'form-control'}),

        }