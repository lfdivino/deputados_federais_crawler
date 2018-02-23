from pymongo import MongoClient


class DeputadosDb(object):
    def __init__(self, mongo_uri, mongo_database, nome_collection):
        self.mongo_uri = mongo_uri
        self.mongo_database = mongo_database
        self.mongo_collection = nome_collection
        self.db_collection = self.conexao_banco_dados()

    def conectar_mongodb_cluster(self):
        client = MongoClient(self.mongo_uri)

        return client

    def conectar_db(self, client_cluster):
        deputados_db = client_cluster.congressmen

        return deputados_db

    def conectar_collection(self, db, nome_collection):
        deputados_collection = db[nome_collection]

        return deputados_collection

    def conexao_banco_dados(self):
        client = self.conectar_mongodb_cluster()
        client_db = self.conectar_db(client)
        client_collection = self.conectar_collection(
            client_db, self.mongo_collection
        )

        return client_collection

    def processar_deputados(self, deputados_db):
        deputados = {
            'Deputados': []
        }
        for deputado in deputados_db:
            del deputado['_id']
            deputados['Deputados'].append(deputado)

        return deputados

    def buscar_deputados(self, nome_deputado=None):
        deputado_domain = {}
        if nome_deputado:
            deputado_domain['nome'] = nome_deputado
            deputado_db = self.db_collection.find_one(deputado_domain)
            if not deputado_db:
                return "Deputado com este nome não foi encontrado!"
            deputados = {
                'Deputados': deputado_db
            }
            del deputados['Deputados']['_id']
        else:
            deputados_db = self.db_collection.find(deputado_domain)
            deputados = self.processar_deputados(deputados_db)

        return deputados

    def buscar_gabinete(self, gabinete):
        deputados = self.db_collection.find_one({'gabinete': gabinete})
        if not deputados:
            return "Gabinete não encontrado!"
        del deputados['_id']

        return deputados

    def buscar_partido(self, partido):
        deputados_db = self.db_collection.find({'partido': partido})
        deputados = self.processar_deputados(deputados_db)

        return deputados

    def buscar_estado(self, estado):
        deputados_db = self.db_collection.find({'uf': estado})
        deputados = self.processar_deputados(deputados_db)

        return deputados
