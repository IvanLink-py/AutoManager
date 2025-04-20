import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QTableWidgetItem
from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtGui import QIcon

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

        self.ui.addDriverAction.triggered.connect(lambda: DB.create_driver(Dialogs.DriverDialog.get_new(self)))
        self.ui.addBusAction.triggered.connect(lambda: DB.create_bus(Dialogs.BusDialog.get_new(self)))
        self.ui.addStopAction.triggered.connect(lambda: DB.create_stop(Dialogs.StopDialog.get_new(self)))

        self.ui.addDriverAction.triggered.connect(self.load_lists)
        self.ui.addBusAction.triggered.connect(self.load_lists)
        self.ui.addStopAction.triggered.connect(self.load_lists)

        self.ui.savePushButton.clicked.connect(self.save_route)
        self.ui.sendPushButton.clicked.connect(self.sent_trip)
        self.ui.endTripPushButton.clicked.connect(self.end_trip)
        self.ui.cancelPushButton.clicked.connect(self.cancel_edit_route)
        self.ui.addRouteStopPushButton.clicked.connect(self.add_route_stop)
        self.ui.routesListWidget.currentRowChanged.connect(self.change_current_route)

        my_icon = QIcon()
        my_icon.addFile('resources/icon.ico')
        self.setWindowIcon(my_icon)

        self.load()

    def load(self):
        self.load_lists()
        self.load_routes()
        self.load_schedule()
        self.load_current_route()
        self.load_current_trips()
        self.load_next_trip()

        self.ui.scheduleTableWidget.contextMenuEvent = self.open_table_menu

    def load_lists(self):
        self.ui.driverComboBox.clear()
        self.ui.busComboBox.clear()
        self.ui.newRouteStopComboBox.clear()

        self.ui.driverComboBox.insertItems(0, [f'{d.last_name} {d.first_name} {d.surname}' for d in DB.get_drivers()])
        self.ui.busComboBox.insertItems(0, [f'{b.mark} - {b.number}' for b in DB.get_busses()])
        self.ui.newRouteStopComboBox.insertItems(0, [f'{b.name}' for b in DB.get_stops()])

    def open_table_menu(self, event):
        menu = QMenu(self)

        menu.addAction("Добавть строку").triggered.connect(self.add_schedule_row)

        menu.exec_(self.ui.scheduleTableWidget.mapToGlobal(event.pos()))

    def add_schedule_row(self):
        sch = Dialogs.ScheduleDialog.get_new(self)
        if sch is None:
            return

        DB.save_schedule(sch)
        self.load_schedule()
        self.load_next_trip()

    def load_schedule(self):
        self.ui.scheduleTableWidget.clearContents()

        __qtablewidgetitem = QTableWidgetItem()
        self.ui.scheduleTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ui.scheduleTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ui.scheduleTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)

        ___qtablewidgetitem = self.ui.scheduleTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442", None));
        ___qtablewidgetitem1 = self.ui.scheduleTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f",
                                                                None));
        ___qtablewidgetitem2 = self.ui.scheduleTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0414\u043d\u0438 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f",
                                                                None));

        for i, schedule in enumerate(DB.get_schedule()):
            self.ui.scheduleTableWidget.insertRow(i)
            self.ui.scheduleTableWidget.setItem(i, 0, QTableWidgetItem(
                f'{schedule.route.name} (остановок: {len(schedule.route.stops)})'))
            self.ui.scheduleTableWidget.setItem(i, 1, QTableWidgetItem(schedule.start_time.strftime("%H:%M")))
            self.ui.scheduleTableWidget.setItem(i, 2, QTableWidgetItem(schedule.week_days))

        self.ui.scheduleTableWidget.resizeColumnsToContents()

    def load_routes(self):
        self.ui.routesListWidget.clear()
        self.ui.routesListWidget.insertItems(0, [f'{b.name}' for b in DB.get_routes()])
        self.ui.routesListWidget.setCurrentRow(0)

    def load_stops(self):
        self.ui.routeStopsListWidget.clear()
        self.ui.routeStopsListWidget.insertItems(0, [f'{s.name}' for s in self.current_route.stops])

    def add_route_stop(self):
        self.current_route.stops.append(DB.get_stops()[self.ui.newRouteStopComboBox.currentIndex()])
        self.load_stops()

    def change_current_route(self, row):
        self.current_route = DB.get_routes()[row]
        self.load_current_route()

    def load_current_route(self):
        self.ui.routeNameLineEdit.setText(self.current_route.name)
        self.load_stops()

    def save_route(self):
        self.current_route.name = self.ui.routeNameLineEdit.text()
        DB.save_route(self.current_route)
        self.load_routes()

    def cancel_edit_route(self):
        self.current_route = models.Route(-1, "", False, [])
        self.load_current_route()

    def sent_trip(self):
        DB.send_trip(
            DB.get_busses()[self.ui.busComboBox.currentIndex()],
            DB.get_drivers()[self.ui.driverComboBox.currentIndex()],
            DB.get_next_trips()[self.ui.nextScheduleListWidget.currentRow()]
        )
        self.load_current_trips()
        self.load_next_trip()

    def load_current_trips(self):
        self.ui.currentTripListWidget.clear()
        self.ui.currentTripListWidget.insertItems(0, [
            f'{t.schedule_id.route.name} (остановок: {len(t.schedule_id.route.stops)}) - {t.schedule_id.start_time.strftime("%H:%M")} ({t.send_time.strftime("%H:%M")})' for
            t in DB.get_actual_trips()])

    def load_next_trip(self):
        self.ui.nextScheduleListWidget.clear()
        self.ui.nextScheduleListWidget.insertItems(0, [
            f'{b.route.name} (остановок: {len(b.route.stops)}) - {b.start_time.strftime("%H:%M")}' for b in
            DB.get_next_trips()])

    def end_trip(self):
        if self.ui.currentTripListWidget.currentRow() == -1:
            return
        DB.end_trip(DB.get_actual_trips()[self.ui.currentTripListWidget.currentRow()], self.ui.tripStatusComboBox.currentText() == "Успешно")
        self.load_current_trips()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
