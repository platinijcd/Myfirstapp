import mysql.connector

dataBase = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = 'admin'
)

#prepare a cursor object
cursorobject = dataBase.cursor()

# create a database
cursorobject.execute("CREATE DATABASE appdb")

print("All done!")

