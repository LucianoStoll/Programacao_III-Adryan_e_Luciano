from django.db import models

# Create your models here.
class Livro(models.Model):
    
    id = models.PositiveIntegerField(unique=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.PositiveIntegerField(default=0)
    disponivel = models.BooleanField(default=True)
    paginas = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.titulo