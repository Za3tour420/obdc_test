# obdc_test
Small test code to try out `pyodbc` module

This code contains basic CRUD functionalites for User class in connection to SQL Server.

Files : 
-user.py
- database.py
- main.py

## Edit line 4 of `main.py` to use the appropriate authentication method :

### Windows authentication : 
```
db = DatabaseManager(server="REPLACE_WITH_YOUR_SERVER", database="REPLACE_WITH_YOUR_DATABASE")
```

### User authentication : 
```
db = DatabaseManager(server="YOUR_SERVER", database="YOUR_DATABASE", trusted_connection="no", uid="YOUR_USERNAME", pwd="YOUR_PASSWORD")
```

## Windows Authentication is used by default.

This code should server as a baseline for more complex project. I may work on something with it in the future :)
