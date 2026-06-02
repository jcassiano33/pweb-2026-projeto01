from django.shortcuts import render

def index(request):
    return render(request, "topplayers/index.html")

def equipe(request):
    equipe = [
        {"foto": "topplayers/assets/img/equipe/raya.png",
         "nome": "David Raya",
         "idade": "30",
         "posição": "Goleiro",
         "nacionalidade": "Espanhol",
        },

        {"foto": "topplayers/assets/img/equipe/nunomendes.png",
         "nome": "Nuno Mendes",
         "idade": "23",
         "posição": "Lateral Esquerdo",
         "nacionalidade": "Português",
        },

        {"foto": "topplayers/assets/img/equipe/gabrielguimalhães.png",
         "nome": "Gabriel Magalhães",
         "idade": "28",
         "posição": "Zagueiro",
         "nacionalidade": "Brasileiro",
        },

        {"foto": "topplayers/assets/img/equipe/saliba.png",
         "nome": "William Saliba",
         "idade": "25",
         "posição": "Zagueiro",
         "nacionalidade": "Francês",
        },

        {"foto": "topplayers/assets/img/equipe/hakimi.png",
         "nome": "Achraf Hakimi",
         "idade": "27",
         "posição": "Lateral Direito",
         "nacionalidade": "Marroquino",
        },

        {"foto": "topplayers/assets/img/equipe/vitinha.png",
         "nome": "Vitinha",
         "idade": "26",
         "posição": "Volante",
         "nacionalidade": "Português",
        },

        {"foto": "topplayers/assets/img/equipe/rice.png",
         "nome": "Rice",
         "idade": "27",
         "posição": "Segundo-volante",
         "nacionalidade": "Inglês",
        },

        {"foto": "topplayers/assets/img/equipe/pedri.png",
         "nome": "Pedri",
         "idade": "23",
         "posição": "Meia ligação",
         "nacionalidade": "Espanhol",
        },

        {"foto": "topplayers/assets/img/equipe/vinijr.png",
         "nome": "Vinícius Júnior",
         "idade": "25",
         "posição": "Ponta Esquerda",
         "nacionalidade": "Brasileiro",
        },

        {"foto": "topplayers/assets/img/equipe/mbappe.png",
         "nome": "Mbappé",
         "idade": "27",
         "posição": "Centroavante",
         "nacionalidade": "Francês",
        },

        {"foto": "topplayers/assets/img/equipe/yamal.png",
         "nome": "Lamine Yamal",
         "idade": "18",
         "posição": "Ponta Direita",
         "nacionalidade": "Espanhol",
        },

        {"foto": "topplayers/assets/img/equipe/ancelotti.png",
         "nome": "Ancelotti",
         "idade": "66",
         "posição": "Técnico",
         "nacionalidade": "Italiano",
        },
    ]
    context = {"equipe": equipe}
    return render(request, "topplayers/equipe.html", context)

def sobre(request):
    return render(request, "topplayers/sobre.html")