from django.db import models

# Create your models here.
class Livro(models.Model):
    
    id = models.PositiveIntegerField(unique=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)
    ano = models.PositiveIntegerField(default=0)
    paginas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo