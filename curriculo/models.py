from django.db import models

# Create your models here.

class Habilidade(models.Model):
    titulo=models.CharField(max_length=120)
    is_learning=models.BooleanField()
    pic=models.ImageField()

class Curso(models.Model):
    titulo=models.CharField(max_length=250)
    instituicao=models.CharField(max_length=120)
    pic=models.ImageField()


