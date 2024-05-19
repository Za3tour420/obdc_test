from database import *

class User:

################################################################################
#### CONSTRUCTOR
################################################################################

    def __init__(self, name, username, email, password):
        self._name = name
        self._username = username
        self._email = email
        self._password = password

################################################################################
#### GETTERS & SETTERS
################################################################################

    def getName(self):
        return self._name
    
    def getUsername(self):
        return self._username
    
    def getEmail(self):
        return self._email
    
    def getPassword(self):
        return self._password
    
    def setName(self, name):
        self._name = name

    def setUsername(self, username):
        self._username = username

    def setEmail(self, email):
        self._email = email

    def setPassword(self, password):
        self._password = password

#################################################################################
#### CRUD
################################################################################

    def addUser(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO [User] (name, username, email, password) VALUES (?, ?, ?, ?);',
                        (self._name, self._username, self._email, self._password))
            connection.commit()
            cursor.close()
            print('User successfully added!')
        except pyodbc.Error as e:
            print('Failed to add user!\n', e)
        

    def updateUser(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute('UPDATE [User] SET password=? WHERE username=?;',
                        (self._password, self._username))
            connection.commit()
            cursor.close()
            print('User successfully updated!')
        except pyodbc.Error as e:
            print('Failed to update user!\n', e)

    def deleteUser(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM [User] WHERE username=? AND email=?;',
                        (self._username, self._email))
            connection.commit()
            cursor.close()
            print('User successfully deleted!')
        except pyodbc.Error as e:
            print('Failed to delete user!\n', e)
    
    def selectUser(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM [User] WHERE name=? AND username=? AND email=? AND password=? ORDER BY username;',
                           (self._name, self._username, self._email, self._password))
            user = cursor.fetchone()
            if user:
                print("User successfully selected!")
                print(user)
            else:
                print("No matching user found!")
        except pyodbc.Error as e:
            print('Failed to select user!\n', e)

def selectAllUsers(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM [User] ORDER BY username;')
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print('No users found!')
    except pyodbc.Error as e:
        print('Failed to select all users!\n', e)