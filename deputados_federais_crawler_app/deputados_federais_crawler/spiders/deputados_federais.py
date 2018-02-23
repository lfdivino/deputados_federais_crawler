import scrapy


class DeputadosFederaisCrawler(scrapy.Spider):
    name = "congressmen"
    pagina_deputados = 'http://www.camara.leg.br/internet/deputado/Dep_Lista.asp?Legislatura=55&Partido=QQ&SX=QQ&Todos=None&UF=QQ&condic=QQ&forma=lista&nome=&ordem=nome&origem=None'
    start_urls = [
        pagina_deputados,
    ]

    def parse_dados_deputado(self, deputado):
        dados_deputados = deputado.css(
            'li::text').extract()[2].strip('\r\n\t').split(' - ')

        nome = deputado.css('a > b::text').extract()[0]
        partido = dados_deputados[0].split(':')[1].split('/')[0].strip()
        uf = dados_deputados[0].split(':')[1].split('/')[1].strip()
        gabinete = dados_deputados[1].split(':')[1].strip()
        anexo = dados_deputados[2].split(':')[1].strip()
        fone = dados_deputados[3].split(':')[1].strip()
        fax = dados_deputados[4].split(':')[1].strip()
        email = deputado.css('a::text').extract()[0]

        return nome, partido, uf, gabinete, anexo, fone, fax, email

    def parse(self, response):
        for deputado in response.css('#demaisInformacoes'):

            nome, partido, uf, gabinete, anexo, fone, fax, email = \
                self.parse_dados_deputado(deputado)

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
