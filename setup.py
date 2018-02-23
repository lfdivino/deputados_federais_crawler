# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='scrapyDeputados',
    version='1.0',
    packages=[
        'deputados_federais_crawler_app',
        'deputados_federais_crawler_app/deputados_federais_crawler',
        'deputados_federais_crawler_app/deputados_federais_crawler/spiders',
        'deputados_federais_crawler_app/tests',
        'deputados_api'
    ],
    url='',
    license='',
    author='Luiz Felipe do Divino',
    author_email='lf.divino@gmail.com',
    description='Modulo para realizar o scrapy dos deputados federais no site da camara'
)
