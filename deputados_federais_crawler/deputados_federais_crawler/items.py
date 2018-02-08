# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DeputadosFederaisCrawlerItem(scrapy.Item):
    nome = scrapy.Field()
    partido = scrapy.Field()
    uf = scrapy.Field()
    gabinete = scrapy.Field()
    anexo = scrapy.Field()
    fone = scrapy.Field()
    fax = scrapy.Field()
    email = scrapy.Field()
