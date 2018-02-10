from pymongo import MongoClient


class DeputadosDb(object):
    def __init__(self, mongo_uri, mongo_database, collection_name):
        self.mongo_uri = mongo_uri
        self.mongo_database = mongo_database
        self.mongo_collection = collection_name
        self.db_collection = self.conexao_banco_dados()

    def connect_to_mongodb_cluster(self):
        client = MongoClient(self.mongo_uri)

        return client

    def connect_db(self, client_cluster):
        congressmen_db = client_cluster.congressmen

        return congressmen_db

    def connect_collection(self, db, collection_name):
        congressmen_collection = db[collection_name]

        return congressmen_collection

    def conexao_banco_dados(self):
        client = self.connect_to_mongodb_cluster()
        client_db = self.connect_db(client)
        client_collection = self.connect_collection(
            client_db, self.mongo_collection
        )

        return client_collection

    def processar_deputados(self, deputados_from_db):
        deputados = {
            'Deputados': []
        }
        for deputado in deputados_from_db:
            del deputado['_id']
            deputados['Deputados'].append(deputado)

        return deputados

    def buscar_deputados(self, nome_deputado=None):
        deputado_domain = {}
        if nome_deputado:
            deputado_domain['nome'] = nome_deputado
            deputado_from_db = self.db_collection.find_one(deputado_domain)
            if not deputado_from_db:
                return "Deputado com este nome não foi encontrado!"
            deputados = {
                'Deputados': deputado_from_db
            }
            del deputados['Deputados']['_id']
        else:
            deputados_from_db = self.db_collection.find(deputado_domain)
            deputados = self.processar_deputados(deputados_from_db)

        return deputados

    def buscar_gabinete(self, gabinete):
        deputados = self.db_collection.find_one({'gabinete': gabinete})
        if not deputados:
            return "Gabinete não encontrado!"
        del deputados['_id']

        return deputados

    def buscar_partido(self, partido):
        deputados_from_db = self.db_collection.find({'partido': partido})
        deputados = self.processar_deputados(deputados_from_db)

        return deputados

    def buscar_estado(self, estado):
        deputados_from_db = self.db_collection.find({'uf': estado})
        deputados = self.processar_deputados(deputados_from_db)

        return deputados
