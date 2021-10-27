from pymongo import MongoClient


class MongoDB:

    @classmethod
    def get_database(cls):
        CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"

        client = MongoClient(CONNECTION_STRING)

        return client['test_db']

    @classmethod
    def insert_data(cls, data):
        dbname = cls.get_database()
        collection_name = dbname["articles"]
        collection_name.insert_one(data)
