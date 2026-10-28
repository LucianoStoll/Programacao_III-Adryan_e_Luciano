from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse, HttpResponse
from .models import Livro

# Create your views here.
def produto(request, idLivro):
    p = get_object_or_404(Livro, id=idLivro)
    return JsonResponse({"id": p.id, "titulo": p.titulo,"autor": p.autor,
    "ano": int(p.ano), "páginas": int(p.paginas),"disponível": bool(p.disponivel)})

def lista_livros(request):
    dados = []
    for p in Livro.objects.all():
        dados.append({"id": p.id, "titulo": p.titulo,"autor": p.autor,
    "ano": int(p.ano), "páginas": int(p.paginas),"disponível": bool(p.disponivel)}) 
    return JsonResponse({"Livros": dados})
