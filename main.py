from user import *

if __name__ == "__main__":
    db = DatabaseManager(server="YOUR_SERVER", database="YOUR_DATABASE")
    print("Connecting to database...")
    connectionManager = db.connectToDatabase()
    if connectionManager:
        print('Successfully connected to database!')

        try:
            user = User('Ahmed Mohsen', 'chleka', 'ahmedmohsen.gmail@com', 'pewpewperpew')
            user.selectUser(connectionManager)
            selectAllUsers(connectionManager)
        finally:
            db.closeConnection()