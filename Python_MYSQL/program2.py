import mysql.connector

host = "localhost"
port = "3306"
uname = "root"
pwd = "Manvith@123"

try:
    db_conn = mysql.connector.connect(host=host, port=port, user=uname, password=pwd)
    print("Connected to Database Successfully")
except Exception as e:
    print(e)

db_cursor = db_conn.cursor()

''' sql1 = "create database pfsd"
 db_cursor.execute(sql1)
 print("Database Created Successfully ")'''
sql2 = "show databases"
db_cursor.execute(sql2)
for db in db_cursor:
    print(db)

