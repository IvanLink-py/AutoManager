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

        self.load()

        self.ui.addDriverAction.triggered.connect(lambda: DB.create_driver(Dialogs.DriverDialog.get_new(self)))
        self.ui.addBusAction.triggered.connect(lambda: DB.create_bus(Dialogs.BusDialog.get_new(self)))
        self.ui.addStopAction.triggered.connect(lambda: DB.create_stop(Dialogs.StopDialog.get_new(self)))

    def load(self):
        self.ui.driverComboBox.insertItems(0, [f'{d.first_name} {d.last_name} {d.surname}' for d in DB.get_drivers()])
        self.ui.busComboBox.insertItems(0, [f'{b.mark} - {b.number}' for b in DB.get_busses()])
        self.ui.newRouteStopComboBox.insertItems(0, [f'{b.name}' for b in DB.get_stops()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')

    window = MainWindow()
    window.show()

    sys.exit(app.exec())