from user import *

if __name__ == "__main__":
    #WINDOWS AUTHENTICATION
    db = DatabaseManager(server="YOUR_SERVER", database="YOUR_DATABASE")
    
    #USER AUTHENTICATION (COMMENT THE LINE ABOVE AND UNCOMMENT THE LINE BELOW)
    #db = DatabaseManager(server="YOUR_SERVER", database="YOUR_DATABASE", trusted_connection="no", uid="YOUR_USERNAME", pwd="YOUR_PASSWORD")
    
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
