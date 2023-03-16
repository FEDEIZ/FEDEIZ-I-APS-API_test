import psycopg2

class PostgresDatabase:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to postgres database")
        except Exception as e:
            print(f"Error connecting to postgres database: {e}")

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print("Disconnected from postgres database")
