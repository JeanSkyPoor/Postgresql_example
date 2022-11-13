from config import *
from secondary_defs import read_data_for_table


def test_create_mobile_table(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            DROP TABLE IF EXISTS mobiles;  

            CREATE TABLE mobiles (
                id serial PRIMARY KEY,
                model_name VARCHAR(50),
                year VARCHAR(4),
                company VARCHAR(50)
            );

            SELECT 'mobiles' FROM INFORMATION_SCHEMA.TABLES;
            """
            )
        assert len(cursor.fetchone()) == 1, "Table is not created"


def test_add_info(connection):
    with connection.cursor() as cursor:
        data = read_data_for_table()

        for item in data:
            cursor.execute(
                f"""INSERT INTO mobiles (model_name, year, company) VALUES
                    {item};"""
                )

        cursor.execute(
            """
            SELECT COUNT(*) from mobiles where model_name = 'Iphone 11'
            """
        )
        assert len(cursor.fetchone()) == 1, "Info is not created in BD"


def test_update_table(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE mobiles
            SET model_name = 'NEW', year = '2029'
            WHERE model_name = 'Huawei P30 Lite'
            """
        )

        cursor.execute(
            """ 
            SELECT COUNT(*) FROM mobiles
            WHERE model_name = 'NEW' and year = '2029' 
            """
        )
        assert len(cursor.fetchone()) == 1, 'Row is not updated'



