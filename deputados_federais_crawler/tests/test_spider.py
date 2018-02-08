import json
import unittest

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from pymongo import MongoClient

from deputados_federais_crawler.deputados_federais_crawler import \
    settings as my_settings
from deputados_federais_crawler.deputados_federais_crawler.spiders.\
    deputados_federais import FederalCongressmenCrawler


class TestSpiders(unittest.TestCase):
    def setUp(self):
        self.execute_crawler()
        self.congressmen_json = self.congressmen_data_json()

    def congressmen_data_json(self):
        congressmen_list = []
        with open('../congressmen_data.json', 'r') as file:
            dados_file = file.read().split("\n")
            for congressman in dados_file:
                if congressman:
                    congressmen_list.append(json.loads(congressman))

        return congressmen_list

    def execute_crawler(self):
        crawler_settings = Settings()
        crawler_settings.setmodule(module=my_settings)
        crawler_process = CrawlerProcess(settings=crawler_settings)
        crawler_process.crawl(FederalCongressmenCrawler)
        crawler_process.start(stop_after_crawl=True)

    def connect_to_collection(self):
        client = MongoClient(my_settings.MONGO_URI)
        congressmen_db = client.congressmen
        congressmen_collection = congressmen_db.congressmen

        return congressmen_collection

    def test_congressmen_not_null(self):
        self.assertIsNotNone(
            self.congressmen_json,
            "There aren't any congressmen data in the json file!"
        )
        self.assertEqual(
            self.congressmen_json[0]['nome'],
            "ABEL MESQUITA JR.",
            "The nome of the first congressman isn't 'ABEL MESQUITA JR.'"
        )
        self.assertEqual(
            self.congressmen_json[0]['gabinete'],
            "248",
            "The gabinete of the first congressman isn't '248"
        )

        congressmen_collection = self.connect_to_collection()
        self.assertIsNotNone(
            congressmen_collection.find_one({'nome': 'ABEL MESQUITA JR.'}),
            "There aren't any congressmen data in the database collection!"
        )


if __name__ == '__main__':
    unittest.main()
