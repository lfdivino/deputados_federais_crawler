import scrapy


class DeputadosFederaisCrawler(scrapy.Spider):
    name = "congressmen"
    pagina_deputados = 'http://www.camara.leg.br/internet/deputado/Dep_Lista_foto.asp?Legislatura=55&Partido=QQ&SX=QQ&Todos=None&UF=QQ&condic=QQ&forma=lista&nome=&ordem=nome&origem=None'
    start_urls = [
        pagina_deputados,
    ]

    def parse_dados_deputado(self, deputado):
        nome = deputado.css('a > b::text').extract()[0]
        foto = deputado.css('img::attr(src)').extract()[0]
        partido = deputado.css('font::text')[0].extract().split('-')[0].strip()
        uf = deputado.css('font::text')[0].extract().split('-')[1].strip()
        gabinete = deputado.css('font::text')[1].extract().split(' ')[1]
        anexo = deputado.css('font::text')[1].extract().split(' ')[3]
        fone = deputado.css('font::text')[2].extract().split(' ')[1]
        fax = deputado.css('font::text')[3].extract().split(' ')[1]
        email = deputado.css('font::text')[4].extract()

        return nome, foto, partido, uf, gabinete, anexo, fone, fax, email

    def parse(self, response):
        for deputado in response.css("#depFoto > td"):
            if not deputado.css('font::attr(color)'):
                nome, foto, partido, uf, gabinete, anexo, fone, fax, email = \
                    self.parse_dados_deputado(deputado)

                yield {
                    'nome': nome,
                    'foto': foto,
                    'partido': partido,
                    'uf': uf,
                    'gabinete': gabinete,
                    'anexo': anexo,
                    'fone': fone,
                    'fax': fax,
                    'email': email
                }
