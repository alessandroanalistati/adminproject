from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Sala
from .forms import SalaForm, SalaFormExcluir
from .entidades import sala
from .services import sala_service


def listar_sala(request):
    salas = sala_service.listar_salas()
    return render(request, 'salas/listar_salas.html', {'salas': salas})


def inserir_sala(request):
    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            obs = form.cleaned_data["obs"]

            sala_nova = sala.Sala(nome=nome, obs=obs)
            sala_service.cadastrar_sala(sala_nova)

            return redirect('app:listar_salas')
    else:
        form = SalaForm()
    return render(request, 'salas/form_sala.html', {'form': form})


def listar_sala_id(request, id):
    sala = sala_service.listar_sala_id(id)

    return render(request, 'salas/lista_sala.html', {'sala': sala})


def editar_sala(request, id):
    sala_antiga = sala_service.listar_sala_id(id)
    form = SalaForm(request.POST or None, instance=sala_antiga)
    if form.is_valid():
        nome = form.cleaned_data["nome"]
        obs = form.cleaned_data["obs"]

        sala_nova = sala.Sala(nome=nome, obs=obs)
        sala_service.editar_sala(sala_antiga, sala_nova)
        return redirect('app:listar_salas')
    return render(request, 'salas/form_sala.html', {'form': form})


def remover_sala(request, id):
    sala = sala_service.listar_sala_id(id)
    if request.method == "POST":
        sala_service.remover_sala(sala)
        return redirect('app:listar_salas')
    return render(request, 'salas/confirma_exclusao.html', {'sala': sala})
