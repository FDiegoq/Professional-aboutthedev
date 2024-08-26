from django.db import models

# Create your models here.

class Habilidade(models.Model):
    titulo=models.CharField(max_length=120)
    is_learning=models.BooleanField()
    descricao=models.TextField()
    pic=models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.titulo

class Curso(models.Model):
    titulo=models.CharField(max_length=250)
    instituicao=models.CharField(max_length=120)
    plataforma=models.CharField(max_length=150)
    pic=models.ImageField(upload_to='cursos/')

    def __str__(self):
        return self.titulo



