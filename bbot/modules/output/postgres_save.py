from bbot.modules.base import BaseModule
from bbot.modules.output.postgres_connection import PostgresConnection

class Scan:
    def __init__(self, scan_id, scan_data):
        self.scan_id = scan_id
        self.scan_data = scan_data

class PostgresModule(BaseModule):
    def __init__(self, scan, *args, **kwargs):
        super().__init__(scan, *args, **kwargs)
        self.db_connection = PostgresConnection(scan=scan)

    def save_results(self, results):
        cursor = self.db_connection.connection.cursor()
        try:
            for result in results:
                cursor.execute("INSERT INTO ScanResult (data, created_at) VALUES (%s, NOW())",
                               (result['data'],))
            self.db_connection.connection.commit()
            print("Data successful saved")
        except Exception as e:
            print(f"Error saving results: {e}")
            self.db_connection.connection.rollback()
        finally:
            cursor.close()
