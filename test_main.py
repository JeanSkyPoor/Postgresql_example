from config import *
import psycopg2


try:
    #connect to exist database
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    #the cursor for performing database operations
    with connection.cursor() as cursor:
        cursor.execute(
           "SELECT version()" 
        )
        print(f"server version is {cursor.fetchone()}")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")


