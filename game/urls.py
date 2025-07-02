# game/urls.py

from django.urls import path
from . import views # Importa as views do seu app
from django.contrib.auth import views as auth_views # Importa as views de autenticação do Django
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # URLs para Autenticação (usando as views embutidas do Django)
    path('login/', auth_views.LoginView.as_view(template_name='game/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # Redireciona para login após logout
    path('register/', views.register, name='register'), # Sua view customizada para registro

    # URL para a seleção de jogos (requer login)
    path('games/', views.game_selection, name='game_selection'),

    # URL da página inicial (pode ser a tela de login ou seleção, a depender da sua lógica)
    path('', auth_views.LoginView.as_view(template_name='game/login.html'), name='home'),

    path('games/drag_and_drop/', login_required(views.drag_and_drop_game), name='drag_and_drop_game'),
    path('games/visual_comparison/', login_required(views.visual_comparison_game), name='visual_comparison_game'),
    path('games/vertices_challenge/', login_required(views.vertices_challenge_game), name='vertices_challenge_game'),
    path('games/quiz/', login_required(views.quiz_game), name='quiz_game'),
    path('games/assemble_figure/', login_required(views.assemble_figure_game), name='assemble_figure_game'),

]