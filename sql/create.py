import mysql.connector as c

db = c.connect(host = "localhost", user = "root", password = "")
cursor = db.cursor()