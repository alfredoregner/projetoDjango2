from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('receita/<int:id>/', views.receita_detail, name='receita_detail'),
    path('pesquisa/', views.pesquisar_receitas, name='pesquisar_receitas'),
]