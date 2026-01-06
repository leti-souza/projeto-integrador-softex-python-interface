from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    municipio = models.CharField(max_length=100)
    pauta = models.CharField(max_length=100)
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo
