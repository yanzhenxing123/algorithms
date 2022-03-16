import pymongo

class Mongo(object):
    def __init__(self, url):
        self.url = url
        self.conn = pymongo.MongoClient(url)

    def __enter__(self):
        return self.get_session()

    def get_session(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

