from django.db import models

class Jogador(models.Model):
    foto = models.ImageField(upload_to="media/")
    nome = models.CharField(max_length=100)
    iniciais_nome = models.CharField(max_length=2)
    idade = models.IntegerField()
    altura = models.FloatField(max_length=3)
    local_nasc = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    iniciais_nac = models.CharField(max_length=2)
    bio = models.TextField(max_length=2000)
    numero = models.IntegerField()
    posicao_generica = models.CharField(max_length=100)
    posicao = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"

    def __str__(self):
        return self.nome

class Informacao(models.Model):
    ano = models.CharField(max_length=4)
    pais_sede = models.CharField(max_length=100)
    quant_pais_sede = models.IntegerField()
    quant_selecoes = models.IntegerField()
    quant_jogos = models.IntegerField()
    n_edicao = models.IntegerField()
    descricao_da_copa_1 = models.TextField(max_length=2000)
    descricao_da_copa_2 = models.TextField(max_length=2000)
    selecoes_favoritas = models.CharField(max_length=100)
    talento_s = models.CharField(max_length=100)
    veterano_s = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Informação"
        verbose_name_plural = "Informações"

    def __str__(self):
        return "Infos"