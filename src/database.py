from mongomock.mongo_client import MongoClient

class InMemoryDatabase:
    _instance = None

    def __new__(cls) -> MongoClient:
        if cls._instance is None:
            client = MongoClient()
            cls._instance = client.get_database('memory_db')
        return cls._instance