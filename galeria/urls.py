from django.urls import path
from galeria.views import index, servicos, sobre, cadastro, contato
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('servicos/', servicos, name='servicos'),  # Página de serviços
    path('sobre/', sobre, name='sobre'),  # Página sobre nós
    path('cadastro/', cadastro, name='cadastro'),  # Página de cadastro
    path('contato/', contato, name='contato'),  # Página de contato
    path('login/', views.login_view, name='login'), # Página de login
    path('register/', views.register, name='register'),  # Página de registro
]
