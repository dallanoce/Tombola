#!/usr/bin/env python
from datetime import datetime

import pandas as pd
import numpy as np

from PyQt6.QtCore import QDateTime, Qt, QTimer, QModelIndex
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget, QTableView, QPlainTextEdit, QMessageBox)

from TombolaTable import TombolaTable


class TombolaNew(QDialog):
    def __init__(self, table_name, parent=None):
        super(TombolaNew, self).__init__(parent)

        self.setWindowTitle("Nuova Tombola")

        self.table_name = table_name
        x = list(range(1, 10))
        x.append(0)
        self.df = pd.DataFrame('_', index=np.arange(9), columns=x)
        self.model = TombolaTable(self.df)
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        self.view.resizeRowsToContents()

        self.create_bottom_right_box()
        self.createBottomRightGroupBox()

        self.save = QPushButton("Salva")
        self.save.setDefault(True)

        topLayout = QHBoxLayout()
        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 3)
        mainLayout.addWidget(self.view, 1, 0,1,2)
        mainLayout.addWidget(self.topLeftGroupBox, 2, 0)
        mainLayout.addWidget(self.log, 2, 1)
        mainLayout.addWidget(self.save, 3, 1)

        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)

        self.setLayout(mainLayout)

    def create_bottom_right_box(self):
        self.topLeftGroupBox = QGroupBox("Nuovo Numero")

        self.number = QLineEdit()

        insert = QPushButton("Inserisci numero")
        insert.setDefault(True)
        remove = QPushButton("Rimuovi numero")
        remove.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(self.number)
        layout.addWidget(insert)
        layout.addWidget(remove)

        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

        insert.clicked.connect(self.insert_number)
        remove.clicked.connect(self.remove_number)

    def createBottomRightGroupBox(self):
        label_1 = QLabel("Log eventi:")

        self.text_area = QPlainTextEdit()
        self.text_area.setReadOnly(True)
        #text_area.setFocusPolicy(Qt.No)
        #message = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(label_1)
        layout.addWidget(self.text_area)
        #layout.addWidget(message)
        self.log = QWidget()
        self.log.setLayout(layout)

        """
        # Event handlers:
        def display_new_messages():
            new_message = server.get(chat_url).text
            if new_message:
                text_area.appendPlainText(new_message)

        def send_message():
            server.post(chat_url, {"name": name, "message": message.text()})
            message.clear()
        """

    def insert_number(self):
        number_tobe_inserted = self.number.text()

        if len(number_tobe_inserted) == 1:
            number_tobe_inserted_old = number_tobe_inserted
            number_tobe_inserted = f'0{number_tobe_inserted}'
            cifra = True
        else:
            cifra=False

        try:
            row = int(number_tobe_inserted[0])
            col = int(number_tobe_inserted[1])
            df_temp = self.df.copy()

            df_temp.at[row, col] = int(number_tobe_inserted)

            self.df = df_temp
            actual_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if cifra:
                self.model.setData(self.model.index(col,row), number_tobe_inserted_old)
                self.text_area.appendPlainText(f'[{actual_time}]: inserito n. {number_tobe_inserted_old}')
            else:
                self.model.setData(self.model.index(col, row), number_tobe_inserted)
                self.text_area.appendPlainText(f'[{actual_time}]: inserito n. {number_tobe_inserted}')


        except:
            self.error_value(number_tobe_inserted)

    def remove_number(self):
        number_tobe_inserted = self.number.text()

        if len(number_tobe_inserted) == 1:
            number_tobe_inserted_old = number_tobe_inserted
            number_tobe_inserted = f'0{number_tobe_inserted}'
            cifra = True
        else:
            cifra=False

        try:
            row = int(number_tobe_inserted[0])
            col = int(number_tobe_inserted[1])
            df_temp = self.df.copy()

            df_temp.at[row, col] = int(number_tobe_inserted)

            self.df = df_temp

            actual_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if cifra:
                self.model.setData(self.model.index(col,row), '_')
                self.text_area.appendPlainText(f'[{actual_time}]: Rimosso n. {number_tobe_inserted_old}')
            else:
                self.model.setData(self.model.index(col, row), '_')
                self.text_area.appendPlainText(f'[{actual_time}]: Rimosso n. {number_tobe_inserted}')
        except:
            self.error_value(number_tobe_inserted)


    def error_value(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("WARNING")
        dlg.setText(f"Inserito valore non valido: {s}")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")
