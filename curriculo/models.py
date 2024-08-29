from django.db import models

# Create your models here.

class Habilidade(models.Model):
    titulo=models.CharField(max_length=120 ,blank=False)
    descricao=models.TextField(blank=False)
    pic=models.ImageField(upload_to='skills/',blank=False)

    def __str__(self):
        return self.titulo

class Curso(models.Model):
    titulo=models.CharField(max_length=250 ,blank=False)
    is_learning=models.BooleanField(blank=False)
    instituicao=models.CharField(max_length=120 ,blank=False)
    plataforma=models.CharField(max_length=150 ,blank=False)
    professor=models.CharField(max_length=100 ,blank=False)
    pic=models.ImageField(upload_to='cursos/' ,blank=False)


    def __str__(self):
        return self.titulo



