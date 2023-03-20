import psycopg2
from config import *
from requests import requestForLogin , requestForReg

connection = psycopg2.connect(
        host=host,
        user = user,
        password=password,
        database=db_name
    )

def addUser(login , password):
    try:
        with connection.cursor as cursor:
            cursor.execute(f"""INSERT INTO users (login , password) VALUES ({login} , {password});""")
    except Exception as e:
        print("[INFO] Error while working with PostgeSQL")

def getUser(login):
    userDATA=[]
    with connection.cursor as cursor:
        login = cursor.execute(f"""SELECT login FROM users WHERE login={login}""")
        password = cursor.execute(f"""SELECT password FROM users WHERE login={login}""")
        userDATA[0] = login
        userDATA[1] = password

try:
    connection.autocommit = True

    with connection.cursor as cursor:
        cursor.execute("""
                CREATE TABLE users(
                id serial PRIMARY KEY ,
                login varchar(50) NOT NULL ,
                password varchar(100) NOT NULL ,
                level varchar(100) DEFAULT 1,
                points varchar(100000) DEFAULT 0,
                role varchar(50) DEFAULT USER);""")

except Exception as e:
    print("[INFO] Error while working with PostgreSQL ",e)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
