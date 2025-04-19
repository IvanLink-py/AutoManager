# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow
from DB import DB


def main():
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    DB()
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
