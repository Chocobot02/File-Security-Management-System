from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import os, sys
import loginUI




if __name__=='__main__':
    app = QApplication(sys.argv)
    main_window = loginUI.loginUI()
    main_window.show()
    sys.exit(app.exec())



