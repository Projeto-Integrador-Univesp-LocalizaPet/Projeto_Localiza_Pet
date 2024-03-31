from django.db import models

# Create your models here.


class PostTeste(models.Model):
    titulo = models.CharField(max_length=250)
    conteudo = models.TextField()
