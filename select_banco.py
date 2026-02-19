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
#VAMOS BUSCAR OS DADOS
with connection:
    with  connection.cursor() as cursor:
        menor_id = input('Digite o menor id ')
        maior_id = input('Digite o maior id ')
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (menor_id, maior_id))
        
        data = cursor.fetchall()
        
        for row in data:
            _id, name, age = row
            print(_id, name, age)

