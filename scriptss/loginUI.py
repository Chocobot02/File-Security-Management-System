from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import os, sys
from PyQt6.QtWidgets import QWidget
from fetch import uisetup

class loginUI(QWidget, uisetup):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setup_ui(self,title='File Security Management System - Login', width=370, height=450) 
        #elements in label_latyout
        self.title = QLabel(self)
        self.title.setText('        FILE SECURITY \nMANAGEMENT SYSTEM') # ayaw ma justify mano mano na lang
        self.title.setStyleSheet('''
        color: white;
        font-weight: bold;
        font-size: 22px;
''')
        self.label = QLabel(self)
        pixmap = QPixmap("./images/content/image").scaled(130,130)
        self.label.setPixmap(pixmap)
        self.label.setStyleSheet('margin-left:50px')

        #elements in loginlayout
        self.labeluser = QLabel(self)
        self.labeluser.setText('Enter Username: ')
        self.labeluser.setStyleSheet('color: white')
        self.username = self.createLabel('    Enter Username')

        self.labelpass = QLabel(self)
        self.labelpass.setText('Enter Password')
        self.labelpass.setStyleSheet('color: white')
        self.passwords = self.createLabel('    Enter Password',password_mode=True)

        self.showpass = QCheckBox(self)
        self.showpass.setText('Show Password')
        self.showpass.stateChanged.connect(lambda state: self.showpassword(state, self.passwords))
        self.showpass.setStyleSheet('color: white')

        #elements in button_layout
        self.logins = QPushButton(self)
        self.logins.setText('Login')
        self.logins.setStyleSheet(self.button_design())
        self.logins.clicked.connect(self.submitinfo)
        
        label_layout = QVBoxLayout()
        label_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_layout.addSpacing(20)
        label_layout.addWidget(self.title)
        label_layout.addWidget(self.label)

        loginlayout = QVBoxLayout()
        loginlayout.addWidget(self.labeluser)
        loginlayout.addWidget(self.username)
        loginlayout.addWidget(self.labelpass)
        loginlayout.addWidget(self.passwords)
        loginlayout.addWidget(self.showpass)
        loginlayout.addSpacing(15)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(label_layout)
        main_layout.addLayout(loginlayout)
        main_layout.addWidget(self.logins)
        main_layout.addSpacing(10)
        self.setLayout(main_layout)

    def submitinfo(self):
        pw = self.passwords.text()
        pw.strip() #remove spaces
        un = self.username.text()
        un.strip()
        if len(pw) == 0:
            QMessageBox.warning(self,'Password Error','Can\'t be empty password!')
        elif pw.isspace():
            QMessageBox.warning(self, 'Password Error', 'invalid pass. No spaces at the beginning!')
        elif un == '123' and pw == '123': #change pass based sa trip == un(username), pw(password)
            try:
                from homepage import MainUI
                self.switchhome = MainUI()
                self.switchhome.show()
                self.close()
            except:
                QMessageBox.warning(self,'Login Error', 'Error while logging in!')
        else:
            QMessageBox.information(self, 'Unknown User', 'User Does Not Exist\nCheck the Password or Username!')

        
