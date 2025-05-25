from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfis'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_tipo_usuario')
    
    def get_tipo_usuario(self, obj):
        return obj.profile.get_tipo_usuario_display() if hasattr(obj, 'profile') else '-'
    get_tipo_usuario.short_description = 'Tipo de Usuário'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
