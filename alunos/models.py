from django.db import models

# Create your models here.

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.estado.sigla})"

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"