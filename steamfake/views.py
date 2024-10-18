from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from steamfake.models import Categoria, Tag

def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")

# Create your views here.
def categoria_index(request: HttpRequest) -> HttpResponse:
    categorias = Categoria.objects.all()
    dados = {
        "categorias": categorias
    }
    return render(request, "categorias/index.html", context=dados)


def categoria_cadastro(request: HttpRequest) -> HttpResponse:

    return render(request, "categorias/cadastro.html")


def categoria_cadastrar(request: HttpRequest) -> HttpResponse:
    nome = request.POST.get("nome")
    categoria = Categoria(nome=nome)
    categoria.save()
    return redirect("categorias")


def categoria_apagar(request:HttpRequest, id: int) -> HttpResponse:
    categoria = Categoria.objects.get(pk=id)
    categoria.delete()
    return redirect("categorias")


def categoria_editar(request:HttpRequest, id:int) -> HttpResponse:
    categoria = Categoria.objects.get(pk=id)
    dados = {
        "categoria": categoria
    }
    return render(request, "categorias/editar.html", context=dados) 


def categoria_editado(request:HttpRequest, id: int) -> HttpResponse:
    nome = request.POST.get("nome")
    categoria = Categoria.objects.get(pk=id)
    categoria.nome = nome
    categoria.save()
    return redirect("categorias")


def tag_index(request: HttpRequest) -> HttpResponse:
    tags = Tag.objects.all()
    dados = {
        "tags": tags
    }
    return render(request, "tags/index.html", context=dados)


def tag_cadastro(request: HttpRequest) -> HttpResponse:

    return render(request, "tags/cadastro.html")


def tag_cadastrar(request: HttpRequest) -> HttpResponse:
    nome = request.POST.get("nome")
    descricao = request.POST.get("descricao")
    tag = Tag(nome=nome, descricao=descricao)
    tag.save()
    return redirect("tags")

def tag_apagar(request:HttpRequest, id: int) -> HttpResponse:
    tag = Tag.objects.get(pk=id)
    tag.delete()
    return redirect("tags")


def tag_editar(request:HttpRequest, id:int) -> HttpResponse:
    tag = Tag.objects.get(pk=id)
    dados = {
        "tag": tag
    }
    return render(request, "tags/editar.html", context=dados) 

def tag_editado(request:HttpRequest, id: int) -> HttpResponse:
    nome = request.POST.get("nome")
    descricao = request.POST.get("descricao")
    tag = Tag.objects.get(pk=id)
    tag.nome = nome
    tag.descricao = descricao
    tag.save()
    return redirect("tags")