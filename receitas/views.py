from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Receita
from .forms import ContatoForm


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

def sobre_nos(request):
    return render(request, 'receitas/sobre_nos.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            send_mail(
                f'Mensagem de {nome}',
                f'Mensagem de {nome} ({email}):\n\n{mensagem}', email, ['seu_email_para_receber@exemplo.com'], fail_silently = False
            )

            return redirect(reverse('sucesso'))
    else:
        form = ContatoForm()

    return render(request, 'receitas/contato.html', {'form' : form})

def sucesso(request):
    return render(request, 'receitas/sucesso.html')

