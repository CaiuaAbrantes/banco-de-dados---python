import pymysql #type: ignore
import dotenv #type: ignore
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with  connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL , '
            'PRIMARY KEY (id)'
            ') ' 
        )
        connection.commit()

    with  connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)' 
            'VALUES(%(n)s, %(i)s) '
        )
        data = ('Joao' , 17)
        data1 = {
            "n" : "Luiz",
            "i" : 27,
        }

        data2 = (
            {'n': 'Caio', 'i':19},
            {'n': 'Julia', 'i':21},
            {'n': 'Tomas', 'i':24},
        )
        #result = cursor.execute(sql, data1)
        result = cursor.executemany(sql, data2)
        connection.commit()
        

    cursor.close()
