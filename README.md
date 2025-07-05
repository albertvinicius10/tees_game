# 🎮 Tees Game

Um jogo educativo interativo desenvolvido em Django para ensinar geometria através de atividades divertidas e responsivas.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/albertvinicius10/tees_game.git
   cd tees_game
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
   ```

4. **Execute as migrações**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

6. **Acesse o projeto**
   ```
   http://127.0.0.1:8000
   ```

## 🎮 Como Jogar

### Jogo de Arraste e Solte
1. Acesse "Arraste e Solte" no menu principal
2. Arraste cada forma para sua categoria correta
3. Use ESC para cancelar o arraste
4. A rolagem funciona automaticamente durante o arraste
5. Verifique suas respostas com o botão "Verificar Respostas"

### Dicas
- **Bordas verdes** = acerto
- **Bordas vermelhas** = erro
- **Rolagem automática** = mova o mouse para as bordas da tela
- **Responsivo** = funciona em desktop, tablet e mobile

---

*Desenvolvido com ❤️ para educação e diversão* 