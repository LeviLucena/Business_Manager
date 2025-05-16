from django import forms
from .models import Cliente, Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'observacoes']
        widgets = {
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'