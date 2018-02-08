import scrapy
from ..items import DeputadosFederaisCrawlerItem


class FederalCongressmenCrawler(scrapy.Spider):
    name = "congressmen"
    congressmen_data_page = 'http://www.camara.leg.br/internet/deputado/Dep_Lista.asp?Legislatura=55&Partido=QQ&SX=QQ&Todos=None&UF=QQ&condic=QQ&forma=lista&nome=&ordem=nome&origem=None'
    start_urls = [
        congressmen_data_page,
    ]

    def parse_congressman_data(self, congressmen):
        congressmen_data = congressmen.css(
            'li::text').extract()[2].strip('\r\n\t').split(' - ')

        nome = congressmen.css('a > b::text').extract()[0]
        partido = congressmen_data[0].split(':')[1].split('/')[0].strip()
        uf = congressmen_data[0].split(':')[1].split('/')[1].strip()
        gabinete = congressmen_data[1].split(':')[1].strip()
        anexo = congressmen_data[2].split(':')[1].strip()
        fone = congressmen_data[3].split(':')[1].strip()
        fax = congressmen_data[4].split(':')[1].strip()
        email = congressmen.css('a::text').extract()[0]

        return nome, partido, uf, gabinete, anexo, fone, fax, email

    def parse(self, response):
        for congressmen in response.css('#demaisInformacoes'):

            nome, partido, uf, gabinete, anexo, fone, fax, email = self.parse_congressman_data(congressmen)

            # item = DeputadosFederaisCrawlerItem()
            # item['nome'] = nome,
            # item['partido'] = partido,
            # item['uf'] = uf,
            # item['gabinete'] = gabinete,
            # item['anexo'] = anexo,
            # item['fone'] = fone,
            # item['fax'] = fax,
            # item['email'] = email,

            yield {
                'nome': nome,
                'partido': partido,
                'uf': uf,
                'gabinete': gabinete,
                'anexo': anexo,
                'fone': fone,
                'fax': fax,
                'email': email
            }
