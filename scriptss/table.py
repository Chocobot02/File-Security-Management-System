from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import os, sys
from PyQt6.QtWidgets import QWidget
from fetch import uisetup, DataFetch


class tableUI(QWidget, uisetup):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setup_ui(self,title='File Security Management System - Table', width=800, height=500) 

        #elements in label_latyout
        self.title = QLabel(self)
        self.title.setText('        Your Secured File') # ayaw ma justify mano mano na lang
        self.title.setStyleSheet('color: white;font-weight: bold;font-size: 40px; padding-top: 20px')
        self.backbutton = QPushButton(self)
        self.backbutton.setText('BACK')
        self.backbutton.clicked.connect(self.goback)

        self.deleteitem = QLabel(self)
        pixmap = QPixmap('./images/content/deleteitem')
        resized_pixmap = pixmap.scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.deleteitem.setPixmap(resized_pixmap)
        self.deleteitem.setStyleSheet('''QLabel{
                                      margin-top: 40px; margin-right: 40px;
                                      } 
                                      QLabel:hover{
                                      border: 1px solid rgba(0,0,0,0.2)
        }''')
        self.deleteitem.mousePressEvent = self.delete_selected_row #astig nito galing kay gpt

        self.table_widget = QTableWidget(self)
        self.table_widget.setFixedHeight(370) 
        self.table_widget.setColumnCount(7) 
        self.table_widget.setHorizontalHeaderLabels(["Files ID","SR-Code", "Student Name", "Username", "File_password", "Application Name", "Profile Status"])
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header = self.table_widget.horizontalHeader()
        self.table_widget.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #908FD2; color: white; font-weight:bold }")

        self.table_widget.cellClicked.connect(self.highlight_row)
        self.table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        elements_layout = QVBoxLayout()
        elements_layout.addWidget(self.title)      
        upper_layout = QHBoxLayout()
        upper_layout.addWidget(self.backbutton)
        upper_layout.addLayout(elements_layout)
        upper_layout.addStretch(1)
        upper_layout.addWidget(self.deleteitem)

        lower_layout = QVBoxLayout()
        lower_layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        lower_layout.addWidget(self.table_widget)

        main_layout = QVBoxLayout()
        main_layout.addLayout(upper_layout)
        main_layout.addStretch(1)
        main_layout.addLayout(lower_layout)
        
        self.setLayout(main_layout)

    def goback(self):
        from homepage import MainUI
        self.home = MainUI()
        self.home.show()
        self.close()

    def load_data_to_table(self, password_condition=None, admin=''):

        if len(password_condition) != 0 and admin != 'adminpass':
            data = DataFetch.fetch_all_data(password_condition=password_condition)
            self.populate_table(data)
        elif len(password_condition) != 0 and admin == 'adminpass':
            data = DataFetch.decrypted_data(password_condition=password_condition)
            self.populate_table(data)

    def populate_table(self, data):
        if data:
            self.table_widget.setRowCount(0)
            for row_index, row_data in enumerate(data):
                self.table_widget.insertRow(row_index)
                for col_index, j in enumerate(row_data):
                    item = QTableWidgetItem(str(j))
                    self.table_widget.setItem(row_index, col_index, item)

    def highlight_row(self, row, col):
        self.table_widget.selectRow(row)
        
    def delete_selected_row(self, event):
        # Get the selected rows
        selected_rows = set(item.row() for item in self.table_widget.selectedItems())

        if not selected_rows:
            QMessageBox.warning(None, 'Warning', 'No row selected!')
            return

        for row in selected_rows:
            #gets the primary key to the selected row
            primary_key_value = self.table_widget.item(row, 0).text()
            DataFetch.delete_from_database(primary_key_value)

        # Remove rows from QTableWidget
        for row in sorted(selected_rows, reverse=True):
            self.table_widget.removeRow(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = tableUI()
    main_window.show()
    sys.exit(app.exec())
        