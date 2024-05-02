from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Caracteristica(models.Model):
    carac = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Caracteristica'

    def __str__(self) -> str:
        return self.carac


class Bichinho_post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    coment = models.TextField()
    # O campo foto por hora é facultativo, mas sera salvo em base64
    foto = models.TextField(null=True, blank=True)
    loc = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    caract = models.ManyToManyField(Caracteristica)


class MyFile(models.Model):
    title = models.CharField(max_length=20)
    arq = models.ImageField(upload_to="img")

    def __str__(self) -> str:
        return self.title
