# -*- coding: utf-8 -*-
import unittest
import api
import requests
import json
import sys

from deputados_federais_crawler_app.tests.constantes_teste import \
    DEPUTADOS_JSON, DEPUTADO_BUSCA_NOME, DEPUTADO_BUSCA_NOME_INEXISTENTE, \
    DEPUTADO_BUSCA_GABINETE, DEPUTADO_BUSCA_GABINETE_INEXISTENTE, \
    DEPUTADO_BUSCA_GABINETE_SEM_NUMERO, DEPUTADOS_BUSCA_PARTIDO, \
    DEPUTADOS_BUSCA_PARTIDO_INEXISTENTE, DEPUTADOS_BUSCA_PARTIDO_SEM_SIGLA, \
    DEPUTADOS_BUSCA_ESTADO, DEPUTADOS_BUSCA_ESTADO_INEXISTENTE, \
    DEPUTADOS_BUSCA_ESTADO_SEM_SIGLA


class TestApiUsandoRequests(unittest.TestCase):
    def test_mostrar_dados_deputados(self):
        resultado = requests.get('http://localhost:5000/api/v1/deputados')
        self.assertEqual(
            resultado.json(), DEPUTADOS_JSON,
            "Resultado do request na API diferente dos dados reais!"
        )


class TestApiUtilizandoRotas(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()

    def test_mostrar_dados_deputados(self):
        resultado = self.app.get('/api/v1/deputados')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADOS_JSON,
            "Resultado do request na API diferente dos dados reais!"
        )

    def test_buscar_deputado_nome(self):
        resultado = self.app.get('/api/v1/deputados/AFONSO MOTTA')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADO_BUSCA_NOME,
            "Resultado da API ao buscar deputado por nome diferente "
            "dos dados reais!"
        )

    def test_buscar_deputado_nome_nao_existente(self):
        resultado = self.app.get('/api/v1/deputados/NOME INEXISTENTE')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADO_BUSCA_NOME_INEXISTENTE,
            "Resultado da API ao buscar deputado por nome diferente "
            "dos dados reais!"
        )

    def test_buscar_deputado_gabinete(self):
        resultado = self.app.get('/api/v1/deputados/gabinete/241')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADO_BUSCA_GABINETE,
            "Resultado da API ao buscar deputado por gabinete diferente "
            "dos dados reais!"
        )

    def test_buscar_deputado_gabinete_inexistente(self):
        resultado = self.app.get('/api/v1/deputados/gabinete/2416')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADO_BUSCA_GABINETE_INEXISTENTE,
            "Resultado da API ao buscar deputado por gabinete diferente "
            "dos dados reais!"
        )

    def test_buscar_deputado_gabinete_sem_numero(self):
        resultado = self.app.get('/api/v1/deputados/gabinete')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADO_BUSCA_GABINETE_SEM_NUMERO,
            "Resultado da API ao buscar deputado por gabinete diferente "
            "dos dados reais!"
        )

    def test_buscar_deputados_partido(self):
        resultado = self.app.get('/api/v1/deputados/partido/pode')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADOS_BUSCA_PARTIDO,
            "Resultado da API ao buscar deputados por partido diferente "
            "dos dados reais!"
        )

    def test_buscar_deputados_partido_inexistente(self):
        resultado = self.app.get('/api/v1/deputados/partido/pxyza')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADOS_BUSCA_PARTIDO_INEXISTENTE,
            "Resultado da API ao buscar deputados por partido diferente "
            "dos dados reais!"
        )

    def test_buscar_deputados_partido_sem_sigla(self):
        resultado = self.app.get('/api/v1/deputados/partido')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADOS_BUSCA_PARTIDO_SEM_SIGLA,
            "Resultado da API ao buscar deputados por partido diferente "
            "dos dados reais!"
        )

    def test_buscar_deputados_estado(self):
        resultado = self.app.get('/api/v1/deputados/estado/mg')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADOS_BUSCA_ESTADO,
            "Resultado da API ao buscar deputados por estado diferente "
            "dos dados reais!"
        )

    def test_buscar_deputados_estado_inexistente(self):
        resultado = self.app.get('/api/v1/deputados/estado/xy')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADOS_BUSCA_ESTADO_INEXISTENTE,
            "Resultado da API ao buscar deputados por estado diferente "
            "dos dados reais!"
        )

    def test_buscar_deputados_estado_sem_sigla(self):
        resultado = self.app.get('/api/v1/deputados/estado')
        self.assertEqual(
            json.loads(resultado.get_data().decode(sys.getdefaultencoding())),
            DEPUTADOS_BUSCA_ESTADO_SEM_SIGLA,
            "Resultado da API ao buscar deputados por estado diferente "
            "dos dados reais!"
        )


if __name__ == '__main__':
    unittest.main()
