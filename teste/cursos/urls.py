from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.lista_cursos, name='lista'),
    path('<int:curso_id>/', views.detalhe_curso, name='detalhe'),
    path('novo/', views.criar_curso, name='criar'),
    path('<int:curso_id>/editar/', views.editar_curso, name='editar'),
    path('<int:curso_id>/inscrever/', views.inscrever_curso, name='inscrever'),
]