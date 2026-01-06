from urllib import request 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Usuario 


#def home(request):
 #   return render(request, 'home/home.html')
 
def home(request):
    if not request.session.get('usuario_email'):
        return redirect('/login/')

    perfil = request.session.get('usuario_perfil')

    return render(request, 'home/home.html', {
        'perfil': perfil
    })

from django.shortcuts import render, redirect
from django.http import HttpResponse

def cadastrar_noticia(request):
    # 1️⃣ verifica se está logado
    if not request.session.get('usuario_email'):
        return redirect('/login/')

    # 2️⃣ verifica o perfil
    perfil = request.session.get('usuario_perfil')

    if perfil not in ['admin', 'reporter']:
        return HttpResponse('Acesso negado')

    # 3️⃣ acesso permitido
    return render(request, 'home/cadastrar_noticia.html')

def lista_noticias(request):
    if not request.session.get('usuario_email'):
        return redirect('/login/')
    
    return render(request, 'home/lista_noticias.html')


def noticias(request):
    
    noticias_fake = [
        {
            'titulo': 'Chuvas intensas atingem o sertão da Paraíba',
            'data': '10/12/2025',
            'fonte': 'G1 Paraíba'
        },
        {
            'titulo': 'Novo hospital é inaugurado em João Pessoa',
            'data': '08/12/2025',
            'fonte': 'Correio da Paraíba'
        },
        {
            'titulo': 'Festival cultural movimenta Campina Grande',
            'data': '05/12/2025',
            'fonte': 'Jornal da Paraíba'
        },
    ]
    return render(request, 'home/noticias.html', {'noticias': noticias_fake})


