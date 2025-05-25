from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    instrutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cursos_criados')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

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
