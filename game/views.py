# game/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Formulário básico de criação de usuário do Django
from django.contrib.auth.decorators import login_required # Decorador para exigir login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Mude para UserCreationForm
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm() # Mude para UserCreationForm
    return render(request, 'game/register.html', {'form': form})


@login_required
def game_selection(request):
    return render(request, 'game/game_selection.html')


@login_required
def drag_and_drop_game(request):
    # Aqui você pode, no futuro, preparar os dados para o jogo
    # Por enquanto, apenas renderizamos o template
    return render(request, 'game/drag_and_drop.html')

@login_required
def visual_comparison_game(request):
    # Por enquanto, não precisamos passar dados específicos do backend.
    # A lógica de geração de figuras e comparação será no frontend (JS).
    return render(request, 'game/visual_comparison.html')
@login_required
def vertices_challenge_game(request):
    # Lógica de geração de figuras e respostas será no frontend (JS).
    return render(request, 'game/vertices_challenge.html')

@login_required
def quiz_game(request):
    # Lógica do quiz será no frontend (JS).
    return render(request, 'game/quiz.html')

@login_required
def assemble_figure_game(request):
    # Lógica do jogo será no frontend (JS).
    return render(request, 'game/assemble_figure.html')