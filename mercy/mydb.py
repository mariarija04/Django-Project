import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'dec25'

	)
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE rose")
print("All Done!")