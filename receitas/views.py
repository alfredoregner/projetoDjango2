from django.shortcuts import render, get_object_or_404
from .models import Receita


def home(request):
    return render(request, 'receitas/home.html')

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk = id)
    context={
        'receita': receita,
    }
    return render(request, 'receitas/receita_detail.html', context)

def pesquisar_receitas(request):
    query = request.GET.get('q') # pega o que foi digitado no campo de busca
    resultados = []

    if query:
        # filtrar receitas que contenham o termo no nome (sem case-sensitive)
        resultados = Receita.objects.filter(title__icontains=query)

    context = {
        'query': query,
        'resultados': resultados,
    }
    return render(request, 'receitas/pesquisa.html', context)