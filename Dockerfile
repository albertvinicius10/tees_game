# Dockerfile (na raiz do seu projeto, onde está manage.py)

# Use uma imagem base Python oficial (Fly.io as suporta bem)
# Prefira uma versão específica para estabilidade
FROM python:3.12-slim-bookworm

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do seu código
COPY . .

# Define variáveis de ambiente do Django
ENV DJANGO_SETTINGS_MODULE=game.settings
ENV PYTHONUNBUFFERED=1

# Expõe a porta que o Django vai rodar (padrão é 8000 para runserver)
EXPOSE 8000

# Comando para rodar as migrações do banco de dados (durante o build)
# CUIDADO: Em produção, migrações no deploy podem ser arriscadas.
# Para apps pequenos e simples, pode ser OK. Para apps maiores, rode migrações separadamente.
RUN python manage.py migrate

# Comando para coletar arquivos estáticos (se você estiver usando Whitenoise)
RUN python manage.py collectstatic --noinput

# Comando padrão para iniciar o servidor Gunicorn (recomendado para produção)
# Instale gunicorn no seu requirements.txt: pip install gunicorn
CMD ["gunicorn", "--bind", ":8000", "game.wsgi:application"]

# Se você não quiser usar Gunicorn para testes rápidos, use runserver, mas NÃO é para produção:
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]