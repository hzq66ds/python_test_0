from elasticsearch import Elasticsearch


class EsJdbc:
    def __init__(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        if str(username) == '':
            self.es = Elasticsearch([ip], port=port)
        else:
            self.es = Elasticsearch([ip], http_auth=(username, password), port=port)

    def indexDatas(self, index, doc_type, dataList):
        for item in dataList:
            self.indexData(index, doc_type, item)

    def indexData(self, index, doc_type, data):
        res = self.es.index(index=index, doc_type=doc_type, body=data)
        print(res, data)

    def getData(self, index, doc_type, did):
        return self.es.get(index=index, doc_type=doc_type, id=did)

    def search(self, index):
        try:
            return self.es.search(index=index, body={"query": {"match_all": {}}})
        except Exception:
            return None

    def delData(self, index, doc_type, did):
        return self.es.delete(index=index, doc_type=doc_type, id=did)


