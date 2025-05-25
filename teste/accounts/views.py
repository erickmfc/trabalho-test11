from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from cursos.models import Curso, Inscricao

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            tipo_usuario = request.POST.get('tipo_usuario')
            Profile.objects.create(user=user, tipo_usuario=tipo_usuario)
            login(request, user)
            return redirect('accounts:painel')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'accounts/login.html')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('accounts:painel')
            else:
                messages.error(request, 'Sua conta está desativada.')
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

@login_required
def perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        
        profile = user.profile
        profile.bio = request.POST.get('bio')
        profile.save()
        
        return redirect('accounts:perfil')
    return render(request, 'accounts/perfil.html')

@login_required
def painel(request):
    user = request.user
    context = {}
    
    if user.profile.tipo_usuario == 'instrutor':
        context['cursos'] = Curso.objects.filter(instrutor=user)
    else:  # aluno
        context['inscricoes'] = Inscricao.objects.filter(aluno=user)
        context['cursos_disponiveis'] = Curso.objects.exclude(
            inscricoes__aluno=user
        )
    
    return render(request, 'accounts/painel.html', context)
