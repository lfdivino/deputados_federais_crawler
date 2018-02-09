import unittest
from pymongo import MongoClient

from deputados_federais_crawler.main import RunCrawler
from deputados_federais_crawler.deputados_federais_crawler import \
    settings as my_settings


class TestSpiders(unittest.TestCase):
    def setUp(self):
        RunCrawler(my_settings)

    def connect_to_mongodb_cluster(self):
        client = MongoClient(my_settings.MONGO_URI)

        return client

    def connect_db(self, client_cluster):
        congressmen_db = client_cluster.congressmen

        return congressmen_db

    def connect_collection(self, db, collection_name):
        congressmen_collection = db[collection_name]

        return congressmen_collection

    def test_congressmen_data(self):
        client_cluster = self.connect_to_mongodb_cluster()
        self.assertIsNotNone(
            client_cluster.nodes,
            "There aren't any valid database!"
        )

        congressmen_db = self.connect_db(client_cluster)
        self.assertEqual(
            congressmen_db.collection_names()[0],
            'congressmen',
            "There isn't the correct collection!"
        )
        congressmen_collection = self.connect_collection(
            congressmen_db, 'congressmen'
        )

        self.assertEqual(
            congressmen_collection.find().count(),
            513,
            "The number of congresmen isn't correct!"
        )

        self.assertIsNotNone(
            congressmen_collection.find_one({'nome': 'ABEL MESQUITA JR.'}),
            "There aren't any congressmen data in the database collection!"
        )


if __name__ == '__main__':
    unittest.main()
