from django.urls import path
from . import views

urlpatterns = [
    path("livros/<int:idLivro>/",views.livro,name="livro")
]