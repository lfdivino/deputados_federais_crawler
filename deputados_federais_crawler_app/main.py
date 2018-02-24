# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings
from twisted.internet import reactor
from multiprocessing import Process, Queue

from deputados_federais_crawler_app.deputados_federais_crawler.spiders.\
    deputados_federais import DeputadosFederaisCrawler


class DeputadosCrawler(object):
    def __init__(self, spider_settings):
        self.spider_settings = spider_settings

    def executar_crawler(self):
        def montar_comandos_crawler(queue_obj):
            try:
                crawler_settings = Settings()
                crawler_settings.setmodule(module=self.spider_settings)
                crawler_runner = CrawlerRunner(
                    settings=crawler_settings).crawl(
                    DeputadosFederaisCrawler
                )
                crawler_runner.addBoth(lambda _: reactor.stop())
                reactor.run()
                queue_obj.put(None)
            except Exception as e:
                queue_obj.put(e)

        queue_obj = Queue()
        processo = Process(target=montar_comandos_crawler, args=(queue_obj,))
        processo.start()
        resultado = queue_obj.get()
        processo.join()

        if resultado is not None:
            raise resultado
