import pyodbc

class DatabaseManager:

    def __init__(self, server, database, trusted_connection='yes', uid=None, pwd=None):
        self._server = server
        self._database = database
        self._trusted_connection = trusted_connection
        self._uid = uid
        self._pwd = pwd
        self._connection = self.connectToDatabase()


    def connectToDatabase(self):
        connectionString = f'DRIVER={{SQL Server}};SERVER={self._server};DATABASE={self._database};\
                            UID={self._uid};PWD={self._pwd};Trusted_Connection={self._trusted_connection}'

        try:
            conn = pyodbc.connect(connectionString)
            return conn
        except pyodbc.Error as e:
            print("Failed to connect to database!\n", e)
            return None
        
    def closeConnection(self):
        if self._connection:
            print("Disconnecting from the database...")
            try:
                self._connection.close()
                print("Disconnected successfully from the database!")
            except pyodbc.Error as e:
                print("Failed to disconnect from database!\n", e)