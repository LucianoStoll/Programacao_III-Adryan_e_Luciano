from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse, HttpResponse
from .models import Livro
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def validar(dados):
    if not dados.get("titulo"):
        return "O título é obrigatório"
    ano = dados.get("ano")
    if not isinstance(ano, (int)) or ano <= 0:
        return "O ano deve ser um número maior que zero"
    paginas = dados.get("paginas", 0)
    if not isinstance(paginas, (int)) or paginas <= 0:
            return "O livro deve ter pelo menos uma página"
    if not dados.get("autor"):
            return "O autor é obrigatório"
    return None

def ler_json(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None

def alterar(request, p):
    dados = ler_json(request)
    if dados is None:
        return JsonResponse({"erro": "JSON inválido"}, status=400)
    erro = validar(dados)
    if erro:
        return JsonResponse({"erro": erro}, status=400)
    p.titulo = dados["titulo"]
    p.autor = dados["autor"]
    p.ano = dados.get("ano")
    p.paginas = dados.get("paginas")
    p.disponivel = dados.get("disponivel")
    p.save()
    return JsonResponse(para_dict(p))

def cadastrar(request):#Tem que mudar muita coisa aqui
    dados = ler_json(request)
    if dados is None:
        return JsonResponse({"erro": "JSON inválido"}, status=400)
    erro = validar(dados)
    if erro:
        return JsonResponse({"erro": erro}, status=400)
    id = dados.get("id")
    if not isinstance(id, int):
        return JsonResponse({"erro": "O ID é obrigatório"}, status=400)
    if Livro.objects.filter(id=id).exists():
        return JsonResponse({"erro": "Já existe um livro com esse ID"}, status=400)
    p = Livro.objects.create(id=id, id=dados["id"],
        preco=dados["preco"], estoque=dados.get("estoque", 0))
    return JsonResponse(para_dict(p), status=201)

@csrf_exempt
def livro(request, idlivro):
    try:
        p = Livro.objects.get(id=idlivro)
    except Livro.DoesNotExist:
        return JsonResponse({"erro": "Livro não encontrado"}, status=404)
    if request.method == "PUT":
        return alterar(request, p)
    if request.method == "DELETE":
        p.delete()
        return HttpResponse(status=204)
    return JsonResponse(para_dict(p))

@csrf_exempt
def lista_livros(request):
    if request.method == "POST":
        return cadastrar(request)
    dados = []
    for p in Livro.objects.all():
        dados.append({"id": p.id, "titulo": p.titulo,"autor": p.autor,
    "ano": int(p.ano), "páginas": int(p.paginas),"disponível": bool(p.disponivel)}) 
    return JsonResponse({"Livros": dados})

