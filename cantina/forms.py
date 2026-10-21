from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome'] 

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        tem_numero = any(char.isdigit() for char in nome)

        if tem_numero: 
            raise forms.ValidationError("Sua mensagem")
        return nome
