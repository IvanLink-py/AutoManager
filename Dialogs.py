import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from ui.ui_BusDialog import Ui_Dialog as ui_BusDialog
from ui.ui_DirverDialog import Ui_Dialog as ui_DriverDialog

class BusDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = ui_BusDialog()
        self.ui.setupUi(self)

class DriverDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = ui_DriverDialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')

    window_1 = BusDialog(None)
    window_1.show()

    window_2 = DriverDialog(None)
    window_2.show()

    sys.exit(app.exec())