#!/usr/bin/env python

import os
import sys
import pandas as pd
from PyQt6.QtCore import QDateTime, Qt, QTimer
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget, QButtonGroup, QTableView, QMainWindow)

from TombolaNew import TombolaNew
from TombolaTable import TombolaTable


class Manager(QMainWindow):
    def __init__(self, parent=None):
        super(Manager, self).__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.originalPalette = QApplication.palette()
        """
        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")
        """

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        # self.createBottomLeftTabWidget()
        # self.createBottomRightGroupBox()
        # self.createProgressBar()

        """
        styleComboBox.textActivated.connect(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)
        """

        topLayout = QHBoxLayout()
        # topLayout.addWidget(styleLabel)
        # topLayout.addWidget(styleComboBox)
        # topLayout.addStretch(1)
        # topLayout.addWidget(self.useStylePaletteCheckBox)
        # topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        # mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        # mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        # mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        # self.setLayout(mainLayout)

        self.central_widget.setLayout(mainLayout)

        self.setWindowTitle("Manager Tombola")
        self.changeStyle('Fusion')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        # self.changePalette()

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) // 100)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Visualizza una vecchia partita")
        layout = QVBoxLayout()

        label_1 = QLabel("Scegli il gioco:")
        self.game_type = QButtonGroup(self)
        radioButton1 = QRadioButton("Tombola")
        radioButton2 = QRadioButton("Superenalotto")
        radioButton1.setChecked(True)
        self.game_type.addButton(radioButton1)
        self.game_type.addButton(radioButton2)

        label_2 = QLabel("Scelgi la partita:")
        self.game_step = QButtonGroup(self)
        radioButton3 = QRadioButton("Partita 1")
        radioButton4 = QRadioButton("Partita 2")
        radioButton3.setChecked(True)
        self.game_step.addButton(radioButton3)
        self.game_step.addButton(radioButton4)

        label_3 = QLabel("Seleziona l'anno tra quelli disponibili:")
        self.year_list = QComboBox()
        files = list(set([f[:4] for f in os.listdir('./data')]))
        for f in files:
            self.year_list.addItem(f)

        load = QPushButton("Carica Risultato")
        load.setDefault(True)

        """
        checkBox = QCheckBox("Tri-state check box")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.CheckState.PartiallyChecked)
        """

        layout.addWidget(label_1)
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)

        layout.addWidget(label_2)
        layout.addWidget(radioButton3)
        layout.addWidget(radioButton4)

        layout.addWidget(label_3)
        layout.addWidget(self.year_list)

        layout.addWidget(load)

        load.clicked.connect(self.load_game)

        # layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    def load_game(self):
        year = self.year_list.currentText()
        type = self.game_type.checkedButton().text()
        step = self.game_step.checkedButton().text()
        try:
            table = f'{year}0815_{type[0].lower()}{step[-1]}.json'
            df = pd.read_json(f'data/{table}')
        except:
            df = pd.DataFrame()

        model = TombolaTable(df)
        self.view = QTableView()
        self.view.setModel(model)
        self.view.resizeColumnsToContents()
        self.view.resizeRowsToContents()
        self.view.show()

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Crea una nuova partita")

        label_1 = QLabel("Scegli il gioco:")
        self.game_type_new = QButtonGroup(self)
        radioButton1 = QRadioButton("Tombola")
        radioButton2 = QRadioButton("Superenalotto")
        radioButton1.setChecked(True)
        self.game_type_new.addButton(radioButton1)
        self.game_type_new.addButton(radioButton2)

        label_2 = QLabel("Scelgi la partita:")
        self.game_step_new = QButtonGroup(self)
        radioButton3 = QRadioButton("Partita 1")
        radioButton4 = QRadioButton("Partita 2")
        radioButton3.setChecked(True)
        self.game_step_new.addButton(radioButton3)
        self.game_step_new.addButton(radioButton4)

        new = QPushButton("Avvia Partita")
        new.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(label_1)
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)

        layout.addWidget(label_2)
        layout.addWidget(radioButton3)
        layout.addWidget(radioButton4)
        layout.addWidget(new)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

        new.clicked.connect(self.new_game)

    def new_game(self):
        year = self.year_list.currentText()
        type = self.game_type_new.checkedButton().text()
        step = self.game_step_new.checkedButton().text()
        table = f'{year}0815_{type[0].lower()}{step[-1]}.json'
        print()
        self.gallery = TombolaNew()
        self.gallery.show()
