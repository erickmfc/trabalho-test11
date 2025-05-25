from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Curso, Inscricao

def lista_cursos(request):
    cursos = Curso.objects.all().order_by('-data_criacao')
    return render(request, 'cursos/lista.html', {'cursos': cursos})

@login_required
def detalhe_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'cursos/detalhe.html', {'curso': curso})

@login_required
def criar_curso(request):
    if request.user.profile.tipo_usuario != 'instrutor':
        messages.error(request, 'Apenas instrutores podem criar cursos.')
        return redirect('cursos:lista')
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        
        if titulo and descricao:
            curso = Curso.objects.create(
                titulo=titulo,
                descricao=descricao,
                instrutor=request.user
            )
            messages.success(request, 'Curso criado com sucesso!')
            return redirect('cursos:detalhe', curso_id=curso.id)
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'cursos/criar.html')

@login_required
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    
    if request.user != curso.instrutor:
        messages.error(request, 'Você não tem permissão para editar este curso.')
        return redirect('cursos:detalhe', curso_id=curso.id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        
        if titulo and descricao:
            curso.titulo = titulo
            curso.descricao = descricao
            curso.save()
            messages.success(request, 'Curso atualizado com sucesso!')
            return redirect('cursos:detalhe', curso_id=curso.id)
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'cursos/editar.html', {'curso': curso})

@login_required
def inscrever_curso(request, curso_id):
    if request.user.profile.tipo_usuario != 'aluno':
        messages.error(request, 'Apenas alunos podem se inscrever em cursos.')
        return redirect('cursos:lista')
    
    curso = get_object_or_404(Curso, id=curso_id)
    
    if Inscricao.objects.filter(aluno=request.user, curso=curso).exists():
        messages.warning(request, 'Você já está inscrito neste curso.')
    else:
        Inscricao.objects.create(aluno=request.user, curso=curso)
        messages.success(request, 'Inscrição realizada com sucesso!')
    
    return redirect('cursos:detalhe', curso_id=curso.id)
