# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_restful import Api, Resource
from werkzeug.serving import run_simple

from deputados_federais_crawler.main import RunCrawler
from deputados_federais_crawler.deputados_federais_crawler import \
    settings as my_settings
from deputados_api.deputados_db import DeputadosDb

app = Flask(__name__)
api = Api(app)

data_base = DeputadosDb(
)


class ScrapyDeputados(Resource):
    def get(self):
        deputados_crawler = RunCrawler(my_settings)
        deputados_crawler.execute_crawler()

        return '200, OK'


class BuscarDeputado(Resource):
    def get(self, nome_deputado):
        if nome_deputado not in ['gabinete', 'estado', 'partido']:
            deputado = data_base.buscar_deputados(nome_deputado)
            deputado = data_base.buscar_deputados(nome_deputado.upper())
        else:
            return "A chamada da rota foi feita de maneira incorreta, " \
                   "o %s não foi informado!" % nome_deputado

        return deputado


class ListaDeputados(Resource):
    def get(self):
        deputados = data_base.buscar_deputados()

        return deputados


class BuscarDeputadoGabinete(Resource):
    def get(self, numero_gabinete=None):
        if numero_gabinete:
            deputados = data_base.buscar_gabinete(numero_gabinete)
        else:
            return "Deve ser inserido o número de um gabinete!"

        return deputados


class BuscarDeputadosPartido(Resource):
    def get(self, partido=None):
        if partido:
            deputados = data_base.buscar_partido(partido.upper())
        else:
            return "Deve ser inserido a sigla de um partido!"

        return deputados


class BuscarDeputadosEstado(Resource):
    def get(self, estado=None):
        if estado:
            deputados = data_base.buscar_estado(estado.upper())
        else:
            return "Deve ser inserido a sigla de um estado!"

        return deputados


api.add_resource(ScrapyDeputados, '/api/v1/scrapy/deputados')
api.add_resource(ListaDeputados, '/api/v1/deputados')
api.add_resource(BuscarDeputado, '/api/v1/deputados/<nome_deputado>')
api.add_resource(
    BuscarDeputadoGabinete, '/api/v1/deputados/gabinete/<numero_gabinete>'
)
api.add_resource(BuscarDeputadosPartido, '/api/v1/deputados/partido/<partido>')
api.add_resource(BuscarDeputadosEstado, '/api/v1/deputados/estado/<estado>')


if __name__ == '__main__':
