import psycopg2
from bbot.modules.base import BaseModule

class PostgresConnection(BaseModule):
    def __init__(self, scan, *args, **kwargs):
        super().__init__(scan, *args, **kwargs)
        self.connection = self.connect_to_db()

    @staticmethod
    def connect_to_db():
        db_config = {
            'dbname': 'everwatch',
            'user': 'ever',
            'password': 'watch',
            'host': 'localhost',
            'port': 5432
        }
        try:
            connection = psycopg2.connect(**db_config)
            print("Connection successful")
            return connection
        except Exception as e:
            print(f"Error connecting to PostgreSQL: {e}")
            return None
