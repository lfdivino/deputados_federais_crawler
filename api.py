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
    os.getenv('MONGO_URI'), os.getenv('MONGO_DATABASE'), 'congressmen'
)


class ScrapyDeputados(Resource):
    def get(self):
        deputados_crawler = RunCrawler(my_settings)
        deputados_crawler.execute_crawler()

        return '200, OK'


class BuscarDeputado(Resource):
    def get(self, nome_deputado):
        deputado = data_base.buscar_deputados(nome_deputado)

        return deputado


class ListaDeputados(Resource):
    def get(self):
        deputados = data_base.buscar_deputados()

        return deputados


class BuscarDeputadoGabinete(Resource):
    def get(self, numero_gabinete):
        deputados = data_base.buscar_gabinete(numero_gabinete)

        return deputados


class BuscarDeputadosPartido(Resource):
    def get(self, partido):
        deputados = data_base.buscar_partido(partido.upper())

        return deputados


class BuscarDeputadosEstado(Resource):
    def get(self, estado):
        deputados = data_base.buscar_estado(estado.upper())

        return deputados


api.add_resource(ScrapyDeputados,'/api/v1/scrapy/deputados')
api.add_resource(ListaDeputados,'/api/v1/deputados')
api.add_resource(BuscarDeputado, '/api/v1/deputados/<nome_deputado>')
api.add_resource(BuscarDeputadoGabinete, '/api/v1/gabinete/<numero_gabinete>')
api.add_resource(BuscarDeputadosPartido, '/api/v1/partido/<partido>')
api.add_resource(BuscarDeputadosEstado, '/api/v1/estado/<estado>')


if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app)
