from config import *



def test_create_mobile_table(connection):
    with connection.cursor() as cursor:
        cursor.execute(
                """CREATE TABLE mobiles (
                    id serial PRIMARY KEY,
                    name VARCHAR(50)
                );"""
            )


