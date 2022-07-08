#!/usr/bin/env python

from PyQt6.QtCore import QAbstractTableModel, QVariant, Qt
import pandas as pd


class TombolaTable(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        #QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        if not index.isValid():
            return QVariant()
        return QVariant(str(self._data.iloc[index.row(), index.column()]))

    def headerData(self, col, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return self._data.columns[col]
