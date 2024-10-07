# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import mysql.connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(273, 433)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 131, 20))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 50, 231, 284))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.user_id_LE = QLineEdit(self.widget)
        self.user_id_LE.setObjectName(u"user_id_LE")

        self.verticalLayout.addWidget(self.user_id_LE)


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.name_LE = QLineEdit(self.widget)
        self.name_LE.setObjectName(u"name_LE")

        self.verticalLayout_2.addWidget(self.name_LE)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.divison_CB = QComboBox(self.widget)
        self.divison_CB.addItem("")
        self.divison_CB.addItem("")
        self.divison_CB.addItem("")
        self.divison_CB.addItem("")
        self.divison_CB.addItem("")
        self.divison_CB.addItem("")
        self.divison_CB.setObjectName(u"divison_CB")

        self.verticalLayout_3.addWidget(self.divison_CB)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.department_CB = QComboBox(self.widget)
        self.department_CB.addItem("")
        self.department_CB.addItem("")
        self.department_CB.addItem("")
        self.department_CB.addItem("")
        self.department_CB.setObjectName(u"department_CB")

        self.verticalLayout_4.addWidget(self.department_CB)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.level_CB = QComboBox(self.widget)
        self.level_CB.addItem("")
        self.level_CB.addItem("")
        self.level_CB.addItem("")
        self.level_CB.addItem("")
        self.level_CB.addItem("")
        self.level_CB.addItem("")
        self.level_CB.setObjectName(u"level_CB")

        self.verticalLayout_5.addWidget(self.level_CB)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.user_level_CB = QComboBox(self.widget)
        self.user_level_CB.addItem("")
        self.user_level_CB.addItem("")
        self.user_level_CB.addItem("")
        self.user_level_CB.addItem("")
        self.user_level_CB.setObjectName(u"user_level_CB")

        self.verticalLayout_6.addWidget(self.user_level_CB)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 350, 231, 27))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_PB = QPushButton(self.widget1)
        self.add_PB.setObjectName(u"add_PB")

        self.horizontalLayout.addWidget(self.add_PB)
        self.add_PB.clicked.connect(self.add_user)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.close)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"User Register", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User Register", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Division", None))
        self.divison_CB.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Divison", None))
        self.divison_CB.setItemText(1, QCoreApplication.translate("MainWindow", u"Admin 1", None))
        self.divison_CB.setItemText(2, QCoreApplication.translate("MainWindow", u"Admin 2", None))
        self.divison_CB.setItemText(3, QCoreApplication.translate("MainWindow", u"Procurement", None))
        self.divison_CB.setItemText(4, QCoreApplication.translate("MainWindow", u"Production", None))
        self.divison_CB.setItemText(5, QCoreApplication.translate("MainWindow", u"SCM", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.department_CB.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Department", None))
        self.department_CB.setItemText(1, QCoreApplication.translate("MainWindow", u"ICM", None))
        self.department_CB.setItemText(2, QCoreApplication.translate("MainWindow", u"HRD", None))
        self.department_CB.setItemText(3, QCoreApplication.translate("MainWindow", u"Procurement TV", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.level_CB.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Level", None))
        self.level_CB.setItemText(1, QCoreApplication.translate("MainWindow", u"Manager", None))
        self.level_CB.setItemText(2, QCoreApplication.translate("MainWindow", u"Assistant Manager", None))
        self.level_CB.setItemText(3, QCoreApplication.translate("MainWindow", u"Supervisor", None))
        self.level_CB.setItemText(4, QCoreApplication.translate("MainWindow", u"Assisstant Supervisor", None))
        self.level_CB.setItemText(5, QCoreApplication.translate("MainWindow", u"Staff", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"User Levell", None))
        self.user_level_CB.setItemText(0, QCoreApplication.translate("MainWindow", u"Select User Level", None))
        self.user_level_CB.setItemText(1, QCoreApplication.translate("MainWindow", u"Super Level", None))
        self.user_level_CB.setItemText(2, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.user_level_CB.setItemText(3, QCoreApplication.translate("MainWindow", u"User", None))

        self.add_PB.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

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

    # insert user
    def insert_user(self):
        try:
            connection = self.create_connection()
            if connection is None:
                return 
            cursor = connection.cursor()
            #buat list user informasi
            self.new_user = [
                self.user_id_LE.text(),
                self.name_LE.text(),
                self.divison_CB.currentText(),
                self.department_CB.currentText(),
                self.level_CB.currentText(),
                self.user_level_CB.currentText(),
            ]

            # insert multiple row ke dalam sql database
            insert_user_query = f"""INSERT INTO user_table (user_id, nama, divisi, department, level, user_level) VALUES (%s, %s, %s, %s, %s, %s)"""

            cursor.execute(insert_user_query, self.new_user)

            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"error:{err}")

    def add_user(self):
        self.insert_user()
        #self.accept()