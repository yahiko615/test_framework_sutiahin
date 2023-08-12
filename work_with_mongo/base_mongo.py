from pymongo import MongoClient


class BaseMongo:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def find_one(self, query):
        return self.collection.find_one(query)

    def find(self, query):
        return self.collection.find(query)

    def delete_one(self, query):
        return self.collection.delete_one(query)

    def sort(self, key, direction):
        if direction == 'asc':
            return self.collection.find().sort(key, 1)
        elif direction == 'desc':
            return self.collection.find().sort(key, -1)

    def update_one(self, query, update):
        return self.collection.update_one(query, update)

    def update_many(self, query, update):
        return self.collection.update_many(query, update)

    def skip(self, num):
        return self.collection.find().skip(num)

    def limit(self, num):
        return self.collection.find().limit(num)
