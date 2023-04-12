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


class MyDB:
    def __init__(self, host, port, user, password, database):
        try:
            self.connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                cursorclass=pymysql.cursors.DictCursor
            )
            print('Connect!')
            self.cursor = self.connection.cursor()
        except Exception as ex:
            print(f'Error  : {ex}')

    def InsertTableBusDriver(self, full_name, salary_id, bus_id):
        insert_query = f'''
            INSERT INTO 
                `{TABLE_BUS_DRIVER}` (full_name, salary_id, bus_id) 
            VALUES 
                ('{full_name}', '{salary_id}', '{bus_id}')
            '''
        self.cursor.execute(insert_query)
        self.connection.commit()

    def InsertTableSalary(self, experience, class_num, salary_sum):
        insert_query = f'''
            INSERT INTO 
                `{TABLE_SALARY}` (experience, class, salary_sum) 
            VALUES 
                ('{experience}', '{class_num}', '{salary_sum}')
            '''
        self.cursor.execute(insert_query)
        self.connection.commit()

    def InsertTableBus(self, state_number, type_id, route_id):
        insert_query = f'''
            INSERT INTO 
                `{TABLE_BUS}` (state_number, type_id, route_id) 
            VALUES 
                ('{state_number}', '{type_id}', '{route_id}')
            '''
        self.cursor.execute(insert_query)
        self.connection.commit()

    def InsertTableBusType(self, type_info, capacity):
        insert_query = f'''
            INSERT INTO 
                `{TABLE_BUS_TYPE}` (type_info, capacity) 
            VALUES 
                ('{type_info}', '{capacity}')
            '''
        self.cursor.execute(insert_query)
        self.connection.commit()

    def InsertTableRoute(self, route_num, time_start, time_end, time_interval, distance):
        insert_query = f'''
            INSERT INTO 
                `{TABLE_ROUTE}` (route_num, time_start, time_end, time_interval, distance) 
            VALUES 
                ('{route_num}', '{time_start}', '{time_end}', '{time_interval}', '{distance}')
            '''
        self.cursor.execute(insert_query)
        self.connection.commit()

    def PrintTableBusType(self):
        select_all_rows = f'SELECT * FROM {TABLE_BUS_TYPE}'
        self.cursor.execute(select_all_rows)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row['type_info'], ' | ', row['capacity'])


        


if __name__ == "__main__":
    DB = MyDB(HOST, PORT, USER, PASS, DB_NAME)
    # DB.InsertTableBusType(type_info = 'ПАЗ-4230 «Аврора»', capacity = '21')
    DB.PrintTableBusType()
    