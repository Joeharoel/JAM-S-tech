from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction 
from User import Ui_MainWindow
import mysql.connector

class MyUserform (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    #conneksi ke mysql server dan membuat database
        self.create_connection()
        
     # membuat user table
        self.create_user_table()
        self.load_user_info()
    # buat database koneksi di dasboard
    def create_connection(self):
    # buat variable 
        host_name = "localhost"
        user_name = "root"
        my_password = ""
        database_name = "User_DB"

        #estabilsh koneksi ke mysql server
        self.mydb = mysql.connector.connect(
            host = host_name,   
            user = user_name,
            passwd = my_password,   
        )

        #buat cursor untuk eksekusi sql query
        cursor = self.mydb.cursor()

        #buat database jika database tidak eksis
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

        #connect untuk membuat database
        self.mydb = mysql.connector.connect(
            host = host_name,        
            user = user_name,
            passwd = my_password,
            database = database_name,
        )

        return self.mydb

    #membuat student table
    def create_user_table(self):
        #membuat cursor untuk eksekusi sql queri

        cursor = self.create_connection().cursor()

        create_user_table_query = f"""
            CREATE TABLE IF NOT EXISTS user_table(
                user_id VARCHAR(15) PRIMARY KEY,
                nama TEXT,
                divisi TEXT,
                department TEXT,
                level TEXT,
                user_level TEXT
            )"""
        cursor.execute(create_user_table_query)

        self.mydb.commit()
        self.mydb.close()

    
    def load_user_info(self):
        self.tableWidget.setRowCount(0)
        cursor = self.create_connection().connect()
        #data = self.get_data_from_table()
        query = "SELECT user_id, nama, divisi, department, level, user_level FROM user_table"
        result = cursor.execute(query)
        for row_index, row_data in enumerate(result):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    self.tableWidget.setItem(row_index, col_index, item)
