from config import *



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

                SELECT 'mobiles' FROM INFORMATION_SCHEMA.TABLES;"""
            )
        assert len(cursor.fetchone()) == 1, "Table is not created"


def test_add_info(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO mobiles (model_name, year, company) VALUES
            ('Huawei P30 Lite', '2020', 'Huawei Technology Company'),
            ('Iphone 11', '2019', 'Apple'),
            ('HONOR X6', '2022', 'HONOR Device Company'),
            ('Xiaomi 12T PRO', '2022', 'Xiaomi Corporation')
            ;
            """
        )

        cursor.execute(
            """
            SELECT COUNT(*) from mobiles where model_name = 'Iphone 11'
            """
        )
        assert len(cursor.fetchone()) == 1, "Info is not created in BD"

