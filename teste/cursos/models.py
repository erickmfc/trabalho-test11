from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    NIVEL_CHOICES = [
        ('iniciante', 'Iniciante'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado')
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    instrutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cursos_criados')
    duracao_horas = models.PositiveIntegerField(help_text='Duração total do curso em horas')
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='iniciante')
    pre_requisitos = models.TextField(blank=True, help_text='Pré-requisitos necessários para o curso')
    objetivos = models.TextField(help_text='Objetivos de aprendizagem do curso')
    publico_alvo = models.TextField(help_text='Público-alvo do curso')
    materiais = models.TextField(blank=True, help_text='Materiais complementares do curso')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['-data_criacao']

class Aula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='aulas')
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    ordem = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.curso.titulo} - {self.titulo}'

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['ordem']

class Inscricao(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inscricoes')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscricoes')
    data_inscricao = models.DateTimeField(auto_now_add=True)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.aluno.username} - {self.curso.titulo}'

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = ['aluno', 'curso']
