from django.urls import path
from . import views

urlpatterns = [
    #Pega livro por ID
    path("livros/<int:idLivro>/",views.livro,name="livro"),
    #Mostra todos
    path("livros/",views.lista_livros,name="lista"),
]