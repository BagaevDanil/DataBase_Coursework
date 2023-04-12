'''
HOST = '127.0.0.1'
USER = 'root'
PASS = ''
DB_NAME = 'coursework_db'
PORT = 3306
'''
HOST = 'mrbaga0j.beget.tech'
USER = 'mrbaga0j_bd'
PASS = 'Danil272'
DB_NAME = 'mrbaga0j_bd'
PORT = 3306

TABLE_BUS_DRIVER = 'BusDriver'
TABLE_SALARY = 'Salary'
TABLE_BUS = 'Bus'
TABLE_BUS_TYPE = 'BusType'
TABLE_ROUTE = 'Route'

import pymysql
import tkinter as tk
import random

try:
    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASS,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Connect!')

    # window.mainloop()
    # cursor = connection.cursor()

    # create table
    # with connection.cursor() as cursor:
    #     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
    #                          " name varchar(32)," \
    #                          " password varchar(32)," \
    #                          " email varchar(32), PRIMARY KEY (id));"
    #     cursor.execute(create_table_query)
    #     print("Table created successfully")

    # insert data
    
    
    with connection.cursor() as cursor:
        # for city in ARR:
        insert_query = f'''
        INSERT INTO 
            `{TABLE_BUS_DRIVER}` (full_name, salary_id, bus_id) 
        VALUES 
            ('Ситников Исак Георгиевич', '0', '1')
            ('Кулаков Родион Мэлсович', '0', '2')
            ('Королёв Адольф Михайлович', '0', '3')
            ('Лапин Сергей Серапионович', '0', '4')
            ('Казаков Ростислав Васильевич', '0', '5')
        '''
        cursor.execute(insert_query)
        connection.commit()

        insert_query = f'''
        INSERT INTO 
            `{TABLE_BUS}` (state_number, type_id, route_id) 
        VALUES 
            ('C244PT', '1', '1')
            ('X182KE', '1', '2')
            ('E760EA', '2', '3')
            ('K189TM', '3', '4')
            ('K189PE', '2', '5')
        '''

        insert_query = f'''
        INSERT INTO 
            `{TABLE_BUS_TYPE}` (type_info, capacity) 
        VALUES 
            ('ПАЗ-3205', '15')
            ('ЛиАЗ-5256', '24')
            ('НефАЗ-5299', '36')
        '''


        insert_query = f'''
        INSERT INTO 
            `{TABLE_ROUTE}` (route_num, time_start, time_end, time_interval, distance) 
        VALUES 
            ('25', '08:00', '23:00', '10', '1000')
            ('34', '11:00', '22:00', '25', '4000')
            ('18', '10:20', '21:40', '55', '5500')
            ('108', '13:50', '23:20', '30', '8000')
            ('64', '6:15', '18:30', '3', '1700')
        '''

        insert_query = f'''
        INSERT INTO 
            `{TABLE_SALARY}` (experience, class, salary_sum) 
        VALUES 
            ('1', '1', '10000')
            ('2', '1', '20000')
            ('2', '1', '20000')
            ('4', '1', '40000')
            ('1', '1', '10000')
        '''


        # insert_query = f"INSERT INTO `test` (title, shows, info) VALUES ('sdfdf', '7865731', '-');"
        
    

    # update data
    # with connection.cursor() as cursor:
    #     update_query = "UPDATE `users` SET password = 'xxxXXX' WHERE name = 'Oleg';"
    #     cursor.execute(update_query)
    #     connection.commit()

    # delete data
    # with connection.cursor() as cursor:
    #     delete_query = "DELETE FROM `users` WHERE id = 5;"
    #     cursor.execute(delete_query)
    #     connection.commit()


    # select all data from table
    
    '''
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `test`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()
        for row in rows:
            print(row['title'], ' -> ', row['info'])
        print("#" * 20)
    '''

except Exception as ex:
    print(f'Error  : {ex}')



# mrbaga0j_BD
# Danil272