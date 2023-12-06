from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import os, sys
import loginUI


'''
defaultuser = 123
defaultpass = 123 
adminpassword = 'adminpass'

-- in login you can change it in login.py --


NOTE: need to install Pyqt6 and mysql.connector firt

This is the file should be executed.

'''

if __name__=='__main__':
    app = QApplication(sys.argv)
    main_window = loginUI.loginUI()
    main_window.show()
    sys.exit(app.exec())



