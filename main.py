# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication

from MainWindow import MainWindow

app = QApplication(sys.argv)
app.setStyle('fusion')
wnd = MainWindow()
wnd.show()
sys.exit(app.exec())