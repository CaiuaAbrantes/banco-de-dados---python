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

#VAMOS APAGAR O USUARIO COM ID 3
with connection:
    with  connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = 3'
        )
        cursor.execute(sql)
        connection.commit()
