import mysql.connector

host = "localhost"
port = "3306"
uname = "root"
pwd = "Manvith@123"

try:
    db_conn = mysql.connector.connect(host=host, port=port, user=uname, password=pwd)
    print('Connected To Database Successfully')
except Exception as e:
    print(e)
