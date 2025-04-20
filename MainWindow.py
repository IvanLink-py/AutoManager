import sys
from PySide6.QtWidgets import QApplication, QMainWindow

import Dialogs
from DB import DB
from ui.ui_MainWindowDesign import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addDriverAction.triggered.connect(self.create_new_driver)

    def create_new_driver(self):
        driver = Dialogs.DriverDialog.get_new(self)

        if driver is None:
            return

        DB.create_driver(driver)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')

    window = MainWindow()
    window.show()

    sys.exit(app.exec())