import sys
from PySide6.QtWidgets import QApplication, QMainWindow

import Dialogs
import models
from DB import DB
from ui.ui_MainWindowDesign import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_route = models.Route(-1, "", False, [])

        self.load()

        self.ui.addDriverAction.triggered.connect(lambda: DB.create_driver(Dialogs.DriverDialog.get_new(self)))
        self.ui.addBusAction.triggered.connect(lambda: DB.create_bus(Dialogs.BusDialog.get_new(self)))
        self.ui.addStopAction.triggered.connect(lambda: DB.create_stop(Dialogs.StopDialog.get_new(self)))

        self.ui.savePushButton.clicked.connect(self.save_route)
        self.ui.addRouteStopPushButton.clicked.connect(self.add_route_stop)



    def load(self):
        self.ui.driverComboBox.insertItems(0, [f'{d.first_name} {d.last_name} {d.surname}' for d in DB.get_drivers()])
        self.ui.busComboBox.insertItems(0, [f'{b.mark} - {b.number}' for b in DB.get_busses()])
        self.ui.newRouteStopComboBox.insertItems(0, [f'{b.name}' for b in DB.get_stops()])

        self.load_routes()

        self.load_stops()

    def load_routes(self):
        self.ui.routesListWidget.clear()
        self.ui.routesListWidget.insertItems(0, [f'{b.name}' for b in DB.get_routes()])

    def load_stops(self):
        self.ui.routeStopsListWidget.clear()
        self.ui.routeStopsListWidget.insertItems(0, [f'{s.name}' for s in self.current_route.stops])

    def add_route_stop(self):
        self.current_route.stops.append(DB.get_stops()[self.ui.newRouteStopComboBox.currentIndex()])
        self.load_stops()

    def save_route(self):
        self.current_route.name = self.ui.routeNameLineEdit.text()
        DB.save_route(self.current_route)
        self.load_routes()

    def update_route(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')

    window = MainWindow()
    window.show()

    sys.exit(app.exec())