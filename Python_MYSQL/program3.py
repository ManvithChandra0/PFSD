import mysql.connector

host = "localhost"
port = "3306"
uname = "root"
pwd = "Manvith@123"
db = "pfsd"

try:
    db_conn = mysql.connector.connect(host=host, port=port, user=uname, password=pwd, database=db)
    print('Connected To Database Successfully')
except Exception as e:
    print(e)

db_cursor = db_conn.cursor()


def createtabel():
    try:
        sql = " create table employee(id int primary key,name varchar(100) not null,gender varchar(10) not null,salary decimal(10,4) not null,department varchar(100) not null) "
        db_cursor.execute(sql)
        print('Table created successfully')

    except Exception as e:
        print(e)


def insertrecord():
    try:
        sql = " insert into employee values(%s,%s,%s,%s,%s) "
        # values = (101, "Manvith", "MALE", 1200.50, "CSE")
        # values = (102, "Chandra", "MALE", 5000.00, "IT")
        # values = (103, "Humesh", "MALE", 1000.50, "ME")
        values = (104, "Abhi", "MALE", 1500.00, "ME")

        db_cursor.execute(sql, values)
        db_conn.commit()
        print(db_cursor.rowcount, "Record(s) Inserted Successfully")
    except Exception as e:
        print(e)


def updaterecord():
    try:
        sql = "update employee set name=%s where id=%s"
        id = 101
        name = "JSK"
        values = (name, id)
        db_cursor.execute(sql, values)
        db_conn.commit()
        print(db_cursor.rowcount, "Record(s) Updated Successfully")
    except Exception as e:
        print(e)


def deleterecord():
    try:
        sql = "delete from employee where id=%s"
        id = 102
        values = (id,)
        db_cursor.execute(sql, values)
        db_conn.commit()
        print(db_cursor.rowcount, "Record(s) Deleted Successfully")
    except Exception as e:
        print(e)


def displayallrecords():
    try:
        sql = "select * from employee"
        db_cursor.execute(sql)
        rows = db_cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def displayrecordbyid():
    try:
        sql = "select * from employee where id=%s"
        id = int(input("Enter Employee ID:"))
        values = (id,)
        db_cursor.execute(sql, values)
        row = db_cursor.fetchone()
        print(row)
        print(row[0], row[1], row[2], row[3], row[4])
    except Exception as e:
        print(e)


# createtabel()
insertrecord()
# updaterecord()
# deleterecord()
# displayallrecords()
# displayrecordbyid()
