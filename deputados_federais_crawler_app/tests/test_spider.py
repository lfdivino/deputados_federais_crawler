# -*- coding: utf-8 -*-
import unittest

from deputados_federais_crawler_app.main import DeputadosCrawler
from deputados_federais_crawler_app.deputados_federais_crawler import \
    settings as my_settings
from deputados_api.deputados_db import DeputadosDb


class TestSpiders(unittest.TestCase):
    def setUp(self):
        crawler = DeputadosCrawler(my_settings)
        crawler.executar_crawler()

    def test_dados_deputados_federais(self):
        """Testar a conexão com o banco de dados e se os dados são semelhantes
         a fonte de onde foram retirados"""
        base_dados = DeputadosDb(
            my_settings.MONGO_URI,
            my_settings.MONGO_DATABASE, 'congressmen'
        )
        client_cluster = base_dados.conectar_mongodb_cluster()
        self.assertIsNotNone(
            client_cluster.nodes,
            "Não há nenhum banco de dados válido!"
        )

        deputados_db = base_dados.conectar_db(client_cluster)
        self.assertEqual(
            deputados_db.collection_names()[0],
            'congressmen',
            "Não existe nenhuma coleção!"
        )
        deputados_collection = base_dados.conectar_collection(
            deputados_db, 'congressmen'
        )

        self.assertEqual(
            deputados_collection.find().count(),
            513,
            "O número de deputados federais está incorreto!"
        )

        self.assertIsNotNone(
            deputados_collection.find_one({'nome': 'ABEL MESQUITA JR.'}),
            "Não há dados de deputados federais nesta coleção!"
        )


if __name__ == '__main__':
    unittest.main()
