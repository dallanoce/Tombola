#!/usr/bin/env python

from PyQt6.QtCore import QAbstractTableModel, QVariant, Qt
import pandas as pd

from PyQt6.QtCore import QDateTime, Qt, QTimer
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget)


class TombolaNew(QDialog):
    def __init__(self, parent=None):
        super(TombolaNew, self).__init__(parent)

        self.createTopLeftGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()

        topLayout = QHBoxLayout()
        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.bottomLeftTabWidget, 1, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        """
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        """

        self.setLayout(mainLayout)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")

        radioButton1 = QRadioButton("Radio button 1")
        radioButton2 = QRadioButton("Radio button 2")
        radioButton3 = QRadioButton("Radio button 3")
        radioButton1.setChecked(True)

        checkBox = QCheckBox("Tri-state check box")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.CheckState.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Policy.Preferred,
                                               QSizePolicy.Policy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)


        self.bottomLeftTabWidget.addTab(tab1, "&Table")

    def createBottomRightGroupBox(self):
            self.bottomRightGroupBox = QGroupBox("Group 3")
            self.bottomRightGroupBox.setCheckable(True)
            self.bottomRightGroupBox.setChecked(True)

            lineEdit = QLineEdit('s3cRe7')
            lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

            spinBox = QSpinBox(self.bottomRightGroupBox)
            spinBox.setValue(50)

            dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
            dateTimeEdit.setDateTime(QDateTime.currentDateTime())

            slider = QSlider(Qt.Orientation.Horizontal, self.bottomRightGroupBox)
            slider.setValue(40)

            scrollBar = QScrollBar(Qt.Orientation.Horizontal, self.bottomRightGroupBox)
            scrollBar.setValue(60)

            dial = QDial(self.bottomRightGroupBox)
            dial.setValue(30)
            dial.setNotchesVisible(True)

            layout = QGridLayout()
            layout.addWidget(lineEdit, 0, 0, 1, 2)
            layout.addWidget(spinBox, 1, 0, 1, 2)
            layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
            layout.addWidget(slider, 3, 0)
            layout.addWidget(scrollBar, 4, 0)
            layout.addWidget(dial, 3, 1, 2, 1)
            layout.setRowStretch(5, 1)
            self.bottomRightGroupBox.setLayout(layout)
