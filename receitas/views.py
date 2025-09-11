from django.shortcuts import render, get_object_or_404
from .models import Receita


def home(request):
    # receitas=Receita.objects.all()
    # return render(request, 'receitas/home.html', {'receitas':receitas})
    # Obtém a categoria do parâmetro da URL (ex: /?categoria=drink)
    categoria_slug = request.GET.get('categoria')

    categorias_choices = [choice[0] for choice in Receita.CATEGORIAS]

    if categoria_slug:
        # Se uma categoria for selecionada, filtrar as receitas
        receitas = Receita.objects.filter(categoria=categoria_slug)
        # Passa a categoria selecionada para o template, útil para destacar o link no menu
        categoria_selecionada = categoria_slug
    else:
        # Se não houver categoria na URL, mostra todas as receitas
        receitas = Receita.objects.all()
        categoria_selecionada = None

    return render(request, 'receitas/home.html', {
        'receitas': receitas,
        'categorias': categorias_choices,
        'categoria_selecionada': categoria_selecionada,
    })

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