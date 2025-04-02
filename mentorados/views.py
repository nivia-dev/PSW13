from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Mentorados, Navigators
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.
    
def mentorados(request):
    if not request.user is authenticate:
        return redirect('login')
    
    if request.method == 'GET':
        navigators = Navigators.objects.filter(user=request.user)
        mentorados = Mentorados.objects.filter(uset=request.user)
        estagios_flat = [i[1] for i in Mentorados.estagio_choices]
        qtd_estagios = []
        
        for i, j in Mentorados.estagio_choices:
            qtd_estagios.append(Mentorados.objects.filter(estagio=i).count())
        
        
        return render(request, 'mentorados.html', {'estagios': Mentorados.estagio_choices, 'navigators': navigators, 
         'mentorados': mentorados, 'estagios_flat': estagios_flat, 'qtd_estagios': qtd_estagios})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        estagio = request.POST.get("estagio")
        navigator = request.POST.get('navigator')
        
        mentorado = Mentorados(
            nome=nome,
            foto=foto,
            estagio=estagio,
            navigator_id=navigator,
            user = request.user
        )
        
        mentorado.save()
        
        messages.add_message(request, constants.SUCCESS, 'Mentorado cadastrado com sucesso.')
        return redirect('mentorados')
