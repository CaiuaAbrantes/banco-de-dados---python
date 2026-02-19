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

#VAMOS EDITAR O NOME DO USUARIO COM ID 1
with connection:
    with  connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome= %s '
            'WHERE id = %s ' 
        )
        cursor.execute(sql, ('Zacaraias', 1))
        connection.commit()
