from django.shortcuts import render, get_object_or_404
from . models import Jogador, Informacao

def index(request):
    context = {
        "jogadores": Jogador.objects.all(),
        "informacao": Informacao.objects.first(),
    }

    return render(request, "topplayers/index.html", context)

def equipe(request):
    context = {
        "jogadores": Jogador.objects.all(),
        "informacao": Informacao.objects.first(),
    }
    
    return render(request, "topplayers/equipe.html", context)

def jogadores(request):
    context = {
        "jogador": get_object_or_404(Jogador)
    }

    return render(request, context)

def informacoes(request):
    context = {
        "informacao": get_object_or_404(Informacao)
    }

    return render(request, context)

def sobre(request):

    autores = [
        {
            "nome": "José Cassiano",
            "foto": "topplayers/assets/img/team/Cassianus.jpg",
            "papel": "Desenvolvedor",
            "descricao": "Responsável pela estrutura do projeto Django, configuração das views, URLs e templates base.",
        },
        
        {
            "nome": "Gustavo Ivo",
            "foto": "topplayers/assets/img/team/gustauvo.jpeg",
            "papel": "Designer",
            "descricao": "Responsável pelo design visual do site, estilização CSS, responsividade e identidade das páginas.",
        },
    ]

    context = {
        "sobre": sobre,
        "autores": autores,
        "informacao": Informacao.objects.first(),
    }

    return render(request, "topplayers/sobre.html", context)