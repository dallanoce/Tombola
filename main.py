import sys

from PyQt6.QtWidgets import QApplication

from Manager import Manager

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gallery = Manager()
    gallery.show()
    sys.exit(app.exec())





