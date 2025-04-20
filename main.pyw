# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow
from DB import DB
import ctypes


def main():
    DB()
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    myappid = 'LinkCom.BusITC.app.1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    main()
