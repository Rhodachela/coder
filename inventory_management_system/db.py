import mysql.connector
from mysql.connector import errorcode

def connection():
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "MySQL.Installer",
            database = "inventory_management"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS inventory_management")
        # print("'Inventory management' database created successfully")
        return mydb, mycursor

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None, None
