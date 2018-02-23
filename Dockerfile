FROM ubuntu:16.04

# Credits.
MAINTAINER Luiz Felipe do Divino "lf.divino@gmail.com"

# Ambiente básico
RUN apt-get update
RUN apt-get install -y -q build-essential
RUN apt-get install -y python3 python3-pip wget
RUN apt-get install -y python3-dev

# Criar um diretório de trabalho.
RUN mkdir deployment

# Instalar virtualenv.
RUN pip3 install virtualenv

# Adicionar arquivo de dependencias.
ADD requirements.txt /deployment/requirements.txt

# Adicionais os arquivos da aplicação.
ADD api.py /deployment/api.py
ADD deputados_api/ /deployment/deputados_api
ADD deputados_federais_crawler_app/ /deployment/deputados_federais_crawler_app
ADD setup.py /deployment/setup.py

# Rodar o virtualenv.
RUN virtualenv /deployment/env/
RUN /deployment/env/bin/pip3 install wheel
RUN /deployment/env/bin/pip3 install -r /deployment/requirements.txt
RUN /deployment/env/bin/pip3 install /deployment/

EXPOSE 8008