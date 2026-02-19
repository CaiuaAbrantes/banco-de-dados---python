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
        sql = (
            f'SELECT * FROM {TABLE_NAME}'
        )
        cursor.execute(sql)
        
        data = cursor.fetchall()
        
        for row in data:
            _id, name, age = row
            print(_id, name, age)