import json
import unittest

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from deputados_federais_crawler.deputados_federais_crawler import \
    settings as my_settings
from deputados_federais_crawler.deputados_federais_crawler.spiders.deputados_federais import \
    FederalCongressmenCrawler


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
        crawler_process.start()

    def test_congressmen_json_not_null(self):
        self.assertIsNotNone(
            self.congressmen_json,
            "There aren't any congressmen data in the json file!"
        )

    def test_first_congressmen_json_data(self):
        self.assertEqual(
            self.congressmen_json[0]['nome'][0],
            "ABEL MESQUITA JR.",
            "The nome of the first congressman isn't 'ABEL MESQUITA JR.'"
        )
        self.assertEqual(
            self.congressmen_json[0]['gabinete'][0],
            "248",
            "The gabinete of the first congressman isn't '248"
        )

if __name__ == '__main__':
    unittest.main()
