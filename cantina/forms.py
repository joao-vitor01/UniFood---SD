from django import forms
from .models import Categoria, Produto

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

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input'}),
            'categoria': forms.Select(attrs={'class': 'form-input'}),
            'preco': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.50'}),

        }
