from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('aluno', 'Aluno'),
        ('instrutor', 'Instrutor'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
    bio = models.TextField(max_length=500, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.get_tipo_usuario_display()}'

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
