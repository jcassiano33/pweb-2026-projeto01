from django.shortcuts import render

def index(request):
    return render(request, "topplayers/index.html")

def equipe(request):
    return render(request, "topplayers/equipe.html")

def sobre(request):
    return render(request, "topplayers/sobre.html")