import psycopg2
from config import *
import pytest


@pytest.fixture(scope="function")
def connection():
    try:
        connection = psycopg2.connect(
            user = user,
            host = host,
            password = password,
            database = database
        )
        
        #позволяет автоматом использовать SQL запрос без connection.commit()
        connection.autocommit = True

        yield connection
        connection.close()
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    