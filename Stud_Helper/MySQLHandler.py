import json
import mysql.connector
from dotenv import load_dotenv
import os
# Create connection with mysql
mydb = mysql.connector.connect(
    # include details of azure sql database app

    host="sql-studwebapp-dev-005.mysql.database.azure.com",
    user="webappadmin",
    password="root@123",
    database="studentdb"
)
mycursor = mydb.cursor()

# Create Database mydatbase
# mycursor.execute("CREATE DATABASE StudentDB")
# mycursor.execute("CREATE TABLE Student(name VARCHAR(255), id INT PRIMARY KEY NOT NULL, age INT(10))")


def insert():
    name = input("\n Enter Name: ")
    id = input("\n Enter ID: ")
    age = input("\n Enter Age:  ")
    # mycursor.execute("INSERT INTO Student(name , id, age) VALUES ("+name+", id, age)")
    mycursor.execute(
        "INSERT INTO Student (name,id,age) VALUES('"+name+"','"+id+"','"+age+"') ")
    mydb.commit()
    print(mycursor.rowcount, "record inserted")


def insertJson(name, id, age):
    Sname = name
    Sid = id
    Sage = age
    mycursor.execute(
        "INSERT INTO Student (name,id,age) VALUES('"+Sname+"','"+Sid+"','"+Sage+"') ")
    mydb.commit()
    print(mycursor.rowcount, "record inserted")


def displayStud():
    mycursor.execute("SELECT * from Student")
    arr = []
    for x in mycursor:
        arr.append(x)
        # break
        # arr.append(x)
    print("arr", arr)
    return arr


def search():
    name = input("Enter Name to Search record")
    mycursor.execute("SELECT * from Student where name = '"+name+"'")
    for x in mycursor:
        print(x)


def searchJson(name):
    Sname = name
    # name = input("Enter Name to Search record")
    mycursor.execute("SELECT * from Student where name = '"+Sname+"'")
    arr = []
    for x in mycursor:
        arr.append(x)
    return arr


def sortID():
    mycursor.execute("SELECT * from Student ORDER BY id ")
    arr = []
    for x in mycursor:
        #  print(x)
        arr.append(x)
    return arr


def sortName():
    mycursor.execute("SELECT * from Student ORDER BY name ")
    arr = []
    for x in mycursor:
        #  print(x)
        arr.append(x)
    return arr


def showTable():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)


def delete():
    mycursor = mydb.cursor()
    r = input("Enter Roll No of Student you wants to delete")
    mycursor.execute("DELETE FROM Student WHERE id='"+r+"' ")
    mydb.commit()
    print("Record deleted Successfully................")


def deleteJson(id):
    mycursor = mydb.cursor()
    r = id
    # print("r", r)
    mycursor.execute("DELETE FROM Student WHERE id='"+r+"' ")
    mydb.commit()
    print("Record deleted Successfully................")

    # mycursor.execute("Select * from stud_info")

    # for x in mycursor:

    #     print(x)


def update():
    mycursor = mydb.cursor()
    id = input("Enter Roll no you wants to update")
    up_nm = input("Enter Updated Name.")
    mycursor.execute("UPDATE Student SET name='"+up_nm+"' where id='"+id+"' ")
    mydb.commit()
    print("Record Updated Successfully................")


def updateJson(id, name, age):
    mycursor = mydb.cursor()
    Sid = id
    up_nm = name
    up_age = age
    mycursor.execute("UPDATE Student SET name='"+up_nm +
                     "', age='"+up_age+"' where id='"+Sid+"' ")
    mydb.commit()
    print("Record Updated Successfully................")
