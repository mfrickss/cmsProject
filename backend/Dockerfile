# Use a imagem oficial do Python
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /code

# Copie o arquivo de dependências e instale
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copie o resto do código da sua aplicação
COPY ./app /code/app

# Comando para rodar a aplicação (Uvicorn)
# --host 0.0.0.0 é crucial para expor o app fora do container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]