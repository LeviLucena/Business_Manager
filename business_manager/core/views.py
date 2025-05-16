from django.shortcuts import render
from .models import Cliente, Produto  # Importe seus modelos

def lista_clientes(request):
    total_clientes = Cliente.objects.count()
    total_produtos = Produto.objects.count()
    
    return render(request, 'core/clientes.html', {
        'total_clientes': total_clientes,
        'total_produtos': total_produtos,
        # Adicione outros contextos conforme necessário
    })