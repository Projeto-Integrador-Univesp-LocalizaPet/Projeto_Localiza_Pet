from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyFile(models.Model):
    title = models.CharField(max_length=20)
    arq = models.ImageField(upload_to="img")

    def __str__(self) -> str:
        return self.title

    def get_arq_url(self):
        return self.arq.url


class Animal_post(models.Model):
    serial = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to="img")
    sit = (
        ('1', 'Adoção'),
        ('0', 'Perdido')
    )
    opcao = models.CharField(max_length=20, choices=sit, default='0')
    descricao = models.TextField(max_length=250, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.serial
