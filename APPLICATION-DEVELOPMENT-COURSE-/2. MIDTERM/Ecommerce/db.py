import mysql.connector

database = mysql.connector.connect(
    user='root',
    passwd='',
    host='localhost'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE ecommerce")
