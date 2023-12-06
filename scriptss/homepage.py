import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

from PyQt6.QtWidgets import QWidget
from fetch import uisetup, DataFetch

class MainUI(QWidget, uisetup):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setup_ui(self,title='File Security Management System', width=600, height=450)
        
        self.title = QLabel(self)
        self.title.setText('        File Security\nManagement System')
        self.title.setStyleSheet('color: white; font-weight: bold; font-size: 40px')
        title_layout = QHBoxLayout()
        title_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_layout.addWidget(self.title)

        self.additem = QLabel(self)
        pixmap = QPixmap('./images/content/additem')
        resized_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.additem.setPixmap(resized_pixmap)
        self.additem_label = QLabel(self)
        self.additem_label.setText('             ADD NEW DATA')
        self.additem_label.setStyleSheet('color: white; font-size: 15px')

        #para maging clickable ang label(img)
        self.additem.setScaledContents(True)
        self.additem.mousePressEvent = self.showaddfiles
        self.additem.setMouseTracking(True)  # Enable mouse tracking to receive hover events
        self.additem.installEventFilter(self)

        self.labelpin = QLabel(self)
        self.labelpin.setText('ENTER PIN TO VIEW FILES')
        self.labelpin.setStyleSheet('color: white; font-weight: bold; font-size: 20px')

        self.pininput = self.createLabel('INPUT PIN', True)
        #ioverride ang fontstyles na nakalagay sa function since need na mas malaki tignan to
        font = self.pininput.font()
        font.setPointSize(16)  # Set the font size to 16 (adjust as needed)
        self.pininput.setFont(font)

        self.adminpin = self.createLabel('INPUT ADMIN PIN(OPTIONAL)', True) 
        font = self.adminpin.font()
        font.setPointSize(12)  # Set the font size to 16 (adjust as needed)
        self.adminpin.setFont(font)

        self.pinbutton = QPushButton(self)
        self.pinbutton.setText('ENTER')
        self.pinbutton.setStyleSheet('''QPushButton{
                        background-color: green;
                        color: white;
                        height: 40px;
                        font-size: 14px;
                        border: none;
                        border-radius: 5px}
                                        
                    QPushButton:hover{
                        background-color: white;
                        color: green;
                        font-size: 17px;
                        border: 1px solid green;
                    }
        ''''')
        self.pinbutton.clicked.connect(self.verifypass)

        image1 = QVBoxLayout()
        image1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image1.addWidget(self.additem)
        image1.addWidget(self.additem_label)

        item1 = QVBoxLayout()
        item1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        item1.addWidget(self.labelpin)
        item1.addWidget(self.pininput)
        item1.addWidget(self.adminpin)
        item1.addSpacing(1)
        item1.addWidget(self.pinbutton)
        item1.addSpacing(15)

        image_button = QHBoxLayout()
        image_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_button.addLayout(image1, Qt.AlignmentFlag.AlignHCenter)
        image_button.addLayout(item1, Qt.AlignmentFlag.AlignHCenter)

        self.quitbuts = QPushButton(self)
        self.quitbuts.setText('EXIT')
        self.quitbuts.setStyleSheet('''
            QPushButton{
                width: 150px;
                height: 40px;
                margin: 0 100;
                background-color: white;
                color: black;
                font-size: 14px;
                border: none;
                border-radius: 5px}
                                
            QPushButton:hover{
                background-color: orange;
                color: white;
                font-size: 17px;
                border: 1px solid orange;
            }
''')
        self.quitbuts.clicked.connect(self.close)

        mainlayout = QVBoxLayout()
        mainlayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        mainlayout.addLayout(title_layout, Qt.AlignmentFlag.AlignHCenter)
        mainlayout.addSpacing(10)
        mainlayout.addLayout(image_button)
        mainlayout.addStretch(1)
        mainlayout.addWidget(self.quitbuts)
        mainlayout.addSpacing(25)
        self.setLayout(mainlayout)

    def showaddfiles(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dialog = AddUi()
            self.dialog.exec()
        
    def eventFilter(self, obj, event):
        if obj == self.additem:
            if event.type() == 10:  
                self.setCursor(Qt.CursorShape.PointingHandCursor)
            elif event.type() == 11:  # QEvent.Type.Leave
                self.setCursor(Qt.CursorShape.ArrowCursor)
        return super().eventFilter(obj, event)
    
    def verifypass(self):
        passintext = self.pininput.text()
        admintext = self.adminpin.text()
        if DataFetch.is_password_valid(passintext):
            try:
                from table import tableUI
                self.new = tableUI()
                self.new.load_data_to_table(passintext, admintext)
                self.new.show()
                self.close()
            except:
                QMessageBox.information(self, 'error', 'unknown error!')

class AddUi(QDialog, uisetup):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setup_ui(self,'Add Files',370,500)
        self.but = QPushButton(self)
        self.but.setText('back')
        self.but.clicked.connect(self.accept)

        self.userinfo_label = QLabel(self)
        self.userinfo_label.setText('User Information')
        self.userinfo_label.setStyleSheet('color: white')

        self.srcode = self.createLabel('Enter SR-Code(for student only)')
        self.username = self.createLabel('Enter User\'s Name')

        self.applicationlabel = QLabel(self)
        self.applicationlabel.setText('Files Information')
        self.applicationlabel.setStyleSheet('color: white')

        self.applicationname = self.createLabel('Enter Application name')
        self.appusername = self.createLabel('Enter your Application\'s Username')
        self.passwords = self.createLabel('Enter your Application\'s Password',password_mode=True)

        self.showpass = QCheckBox(self)
        self.showpass.setText('Show Password')
        self.showpass.stateChanged.connect(lambda state: self.showpassword(state, self.passwords))
        self.showpass.setStyleSheet('color: white')
        
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        login_layout = QVBoxLayout()
        login_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        login_layout.addSpacing(40)
        login_layout.addWidget(self.userinfo_label)
        login_layout.addWidget(self.srcode)
        login_layout.addSpacing(20)
        login_layout.addWidget(self.username)
        login_layout.addSpacing(20)
        login_layout.addWidget(self.line)
        login_layout.addWidget(self.applicationlabel)
        login_layout.addWidget(self.applicationname)
        login_layout.addSpacing(20)
        login_layout.addWidget(self.appusername)
        login_layout.addSpacing(20)
        login_layout.addWidget(self.passwords)
        login_layout.addWidget(self.showpass)
        login_layout.addSpacing(20)

        buts_layout = QHBoxLayout()
        self.reset = QPushButton(self)
        self.reset.setText('RESET')
        self.reset.clicked.connect(self.resetinput)
        self.reset.setFixedSize(170,50)
        buts_layout.addWidget(self.reset)

        self.add = QPushButton(self)
        self.add.setText('ADD DATA')
        self.add.clicked.connect(self.addtodatabase)
        self.add.setFixedSize(170,50)
        buts_layout.addWidget(self.add)

        mainlayout = QVBoxLayout()
        mainlayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        mainlayout.addLayout(login_layout)
        mainlayout.addStretch(1)
        mainlayout.addLayout(buts_layout)
        mainlayout.addSpacing((30))
        self.setLayout(mainlayout)
    
    def addtodatabase(self):
        srcode = self.srcode.text().strip()
        student_name = self.username.text().strip()
        appuser = self.appusername.text().strip()
        apppass = self.passwords.text().strip()
        application = self.applicationname.text().strip()

        if len(appuser) == 0 or len(apppass) == 0 or len(application) ==0 or len(student_name) == 0:
            QMessageBox.information(self, 'input error', "Application's name,password, or username can not be empty")
        else:
            DataFetch.add_to_database(srcode,student_name,appuser,apppass,application)
    
