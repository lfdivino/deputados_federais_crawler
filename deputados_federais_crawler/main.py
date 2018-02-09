from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings
from twisted.internet import reactor

from deputados_federais_crawler.deputados_federais_crawler.spiders.\
    deputados_federais import FederalCongressmenCrawler


class RunCrawler(object):
    def __init__(self, spider_settings):
        self.spider_settings = spider_settings

    def execute_crawler(self):
        crawler_settings = Settings()
        crawler_settings.setmodule(module=self.spider_settings)
        crawler_runner = CrawlerRunner(settings=crawler_settings).crawl(FederalCongressmenCrawler)
        crawler_runner.addBoth(lambda _: reactor.stop())
        reactor.run()
