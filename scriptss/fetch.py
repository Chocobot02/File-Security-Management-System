from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import os, sys
import mysql.connector
#dito na magfefetch ng sql
class DataFetch:
    
    @staticmethod
    def connect_to_database():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='12345', 
                database='Secured_Files',
                port=3306
            )
            return connection
        except mysql.connector.Error as e:
            QMessageBox.warning(None, 'Connection Error', 'Connection Failed')
            return None

    '''
    Abstraction dito ay ang user doesn't need to know the inner workings of the MySQL 
    connection or query execution; they work with high-level operations like connecting, 
    executing queries, and fetching results. The details of how these operations are 
    implemented are abstracted away since kinocall natin din ito sa ibang script as a func only
    '''
    @staticmethod
    def add_to_database(srcode, studname, aname, apass, appname):
        # Get data from parameters
        studentcode = srcode
        user_name = studname
        appuser = aname
        apppass = apass
        applicationname = appname

        # Perform database insertion
        connection = DataFetch.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO securedfiles (srcode, student_name, application_name, app_password, username) VALUES (%s, %s, %s, %s, %s)"
                values = (studentcode, user_name, appuser, apppass, applicationname)

                cursor.execute(query, values)
                connection.commit()
                QMessageBox.information(None, 'Complete', 'Data has been Added!')

            except mysql.connector.Error as e:
                QMessageBox.warning(None, 'Error', 'Can\'t Add Data! Check inputs')

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    @staticmethod
    def fetch_all_data(password_condition=None):
        connection = DataFetch.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor() 
                if password_condition:
                    query = "SELECT inputfiles_id, srcode, student_name, application_name, username, LPAD('*', CHAR_LENGTH(app_password), '*') AS obscured_password, profile_status FROM securedfiles WHERE app_password = %s"
                    cursor.execute(query, (password_condition,))
                else:
                    query = "SELECT * FROM securedfiles"
                    cursor.execute(query)
                
                data = cursor.fetchall()
                return data

            except mysql.connector.Error as e:
                QMessageBox.warning(None, 'Error', f'Error fetching data: {e}')

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    @staticmethod
    def decrypted_data(password_condition=None):
        connection = DataFetch.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor() 
                if password_condition:
                    query = "SELECT * FROM securedfiles WHERE app_password = %s"
                    cursor.execute(query, (password_condition,))
                else:
                    query = "SELECT * FROM securedfiles"
                    cursor.execute(query)
                
                data = cursor.fetchall()
                return data

            except mysql.connector.Error as e:
                QMessageBox.warning(None, 'Error', f'Error fetching data: {e}')

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
    
    @staticmethod
    def delete_from_database(primary_key_value):
        try:
            connection = DataFetch.connect_to_database()
            if connection:
                cursor = connection.cursor()

                # DELETE query
                delete_query = "DELETE FROM securedfiles WHERE inputfiles_id = %s"
                cursor.execute(delete_query, (primary_key_value,))

                connection.commit()
                QMessageBox.information(None, 'Complete', 'Row has been deleted from the database!')

        except mysql.connector.Error as e:
            QMessageBox.warning(None, 'Error', f'Error deleting row from the database: {e}')

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def is_password_valid(entered_password):
        connection = DataFetch.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT COUNT(*) FROM securedfiles WHERE app_password = %s"
                cursor.execute(query, (entered_password,))
                count = cursor.fetchone()[0]
                return count > 0

            except mysql.connector.Error as e:
                QMessageBox.warning(None, 'Error', f'Error checking password: {e}')

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        return False
    
# since it will use multiple times, it is create to be inherit
class uisetup:
    def center_on_screen(self):
        # Center the main window on the screen
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()
        size = self.geometry()
        self.move(
            screen_geometry.center().x() - size.width() // 2,
            screen_geometry.center().y() - size.height() // 2
        )

    @staticmethod
    def setup_ui(window, title:str, width:int, height:int, iconpath:str='./images/favicon.png', bgpath='./images/bg.png'): #add an argumemnt(path) when you want to change the icon and bg
        window.setWindowTitle(title)
        window.setFixedSize(width, height)

        pixmap1 = QPixmap(iconpath)
        icon = QIcon(pixmap1)
        QApplication.setWindowIcon(icon)

        background = QLabel(window)
        pxm = QPixmap(os.path.abspath(bgpath))
        background.setPixmap(pxm)
        background.setGeometry(0, 0, width, height)

    #dami kase qlineedit dito kaya gawa na lang func  
    def createLabel(self, text, password_mode=False, style ='border-radius: 13px;'):
        if password_mode:
            line_edit = QLineEdit(self)# f password_mode is True, create a qlineedrt in Password mode
            line_edit.setEchoMode(QLineEdit.EchoMode.Password)
            line_edit.setPlaceholderText(text)
            line_edit.setStyleSheet(style)
            line_edit.setFixedSize(300,40)
            return line_edit
        else:
            line_edit_n = QLineEdit(self) # if password_mode is False, create a regular qlineedrt
            line_edit_n.setPlaceholderText(text)
            line_edit_n.setStyleSheet('border-radius: 13px;')
            line_edit_n.setFixedSize(300,40)
            return line_edit_n
        
    def showpassword(self, state, element):
        if state != 2:
            element.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            element.setEchoMode(QLineEdit.EchoMode.Normal)

    def resetinput(self):
        self.srcode.clear()
        self.username.clear()
        self.applicationname.clear()
        self.appusername.clear()
        self.passwords.clear()

    def button_design(self, width= 120, height=40):
        return f'''
            QPushButton{{
                width: {width}px;
                height: {height}px;
                margin: 0 100;
                background-color: white;
                color: green;
                font-size: 14px;
                border: none;
                border-radius: 5px}}
                                
            QPushButton:hover{{
                background-color: green;
                color: white;
                font-size: 17px;
                border: 1px solid green;
            }}
'''