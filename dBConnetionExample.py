import mysql.connector


def open_connection():       
    my_db = mysql.connector.connect(
      host="HOSTADRESS",
      user="USERNAME",
      passwd="PASSWORD",
      database="DATABASE"
    )
    return my_db


def close_connection(my_db):
    my_db.close()
