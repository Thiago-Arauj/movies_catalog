from django.shortcuts import render, get_object_or_404
from core.models import Filme


def home(request):
    all_movies = Filme.objects.filter(id__lte=6)
    to_send = []
    for movie in all_movies:
        filme = {}
        filme['id'] = movie.id
        filme['titulo'] = movie.titulo
        filme['descricao'] = movie.descricao
        filme['ano_lancamento'] = movie.ano_lancamento
        filme['imagem'] = movie.imagem

        to_send.append(filme)

    context = {
        'filmes': to_send
    }

    return render(request, 'index.html', context)


def single_movie(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    context = {
        "filme": filme
    }

    return render(request, 'detail_movie.html', context)


def list_all(request):
    all_movies = Filme.objects.all()
    to_send = []
    for movie in all_movies:
        filme = {}
        filme['id'] = movie.id
        filme['titulo'] = movie.titulo
        filme['descricao'] = movie.descricao
        filme['ano_lancamento'] = movie.ano_lancamento
        filme['imagem'] = movie.imagem

        to_send.append(filme)

    context = {
        'filmes': to_send
    }

    return render(request, 'list_all.html', context)
