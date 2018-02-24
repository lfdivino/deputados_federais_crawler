Deputados Crawler
=================

Esta api foi desenvolvida para o scraping das informações dos deputados federais que estão em exercício no ano de 2018.

Página dos deputados no site da câmara dos deputados:
Website_

Ferramentas Utilizadas
======================

Para esta api foram utilizadas as seguintes ferramentas:

- Scrapy Framework
- Flask
- MongoDB (Atlas_)
- Docker

Instalação
==========

Primeiramente é necessário clonar este repositório e depois acessar a pasta raiz do projeto

1 - Instalação em virtualenv local
=================================

Para instalar a aplicação localmente basta rodar o comando na pasta raiz ::

    ./instalador.sh

Após o término da instalação é necessário ativar o virtualenv criado utilizando o comando ::

    source bin/activate

Assim basta utilizar o seguinte comando para iniciar a API ::

    python deputados_api/api.py

Para rodar os testes unitários basta utilizar o seguinte comando ::

    python deputados_federais_crawler_app/tests/test_spider.py
    python deputados_federais_crawler_app/tests/test_api.py

2 - Instalação via Docker
=========================

Para a instalação da api basta rodar o comando build do Docker na pasta raiz do projeto onde está o Dockerfile ::

    sudo docker build --no-cache -t api_deputados .

Para executar a api através do Docker basta executar o comando run também na pasta raiz do projeto ::

    sudo docker run --env-file env.list -it -p 5000:5000 api_deputados /deployment/env/bin/python /deployment/api.py

Para executar os testes através do Docker basta executar o comando run também na pasta raiz do projeto ::

    sudo docker run --env-file env.list -it -p 5000:5000 api_deputados /deployment/env/bin/python /deployment/deputados_federais_crawler_app/tests/test_spider.py

Rotas da API
============

A api desenvolvida foi separada nas seguintes rotas:

- /api/v1/scrapy/deputados
- /api/v1/deputados
- /api/v1/deputados/<nome_deputado>
- /api/v1/deputados/gabinete/<numero_gabinete>
- /api/v1/deputados/partido/<partido>
- /api/v1/deputados/estado/<estado>

A rota '/api/v1/scrapy/deputados' serve para disparar o crawler para capturar as informações dos deputados na página da câmara dos deputas
e depois salvar estes dados no banco de dados mongo da cloud Atlas.

As demais rotas são para específicas consultas nesse banco de dados.

Maintainers
-----------

- Luiz_ Felipe_ Divino_ (owner)

.. Deputados Crawler links
.. _Website: http://www.camara.leg.br/internet/deputado/Dep_Lista_foto.asp?Legislatura=55&Partido=QQ&SX=QQ&Todos=None&UF=QQ&condic=QQ&forma=lista&nome=&ordem=nome&origem=None

.. Ferramentas Utilizadas links
.. _Atlas: https://cloud.mongodb.com/

.. Maintainers links
.. _Luiz: https://github.com/lfdivino
.. _Felipe: https://github.com/lfdivino
.. _Divino: https://github.com/lfdivino