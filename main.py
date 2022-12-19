HOST = '127.0.0.1'
USER = 'root'
PASS = ''
DB_NAME = 'coursework_db'
PORT = 3306

import pymysql

try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASS,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('WIN!!!!')
except Exception as ex:
    print(f'Error! : {ex}')
