# Usamos a versão slim para manter a imagem leve
FROM python:3.12-slim

# Impede que o Python escreva arquivos .pyc e permite log em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependências de sistema para o PostgreSQL e compilação
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalação das dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante do projeto
COPY . .

EXPOSE 8000