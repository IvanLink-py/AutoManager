import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

import models
from DB import DB
from ui.ui_BusDialog import Ui_Dialog as ui_BusDialog
from ui.ui_DirverDialog import Ui_Dialog as ui_DriverDialog
from ui.ui_StopDialog import Ui_Dialog as ui_StopDialog
from ui.ui_ScheduleDialog import Ui_Dialog as ui_ScheduleDialog


class BusDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = ui_BusDialog()
        self.ui.setupUi(self)

    @staticmethod
    def get_new(parent):
        dialog = BusDialog(parent)
        dialog.exec()
        if dialog.result() == QDialog.DialogCode.Rejected:
            return None
        return models.Bus(-1, dialog.ui.lineEdit.text(), dialog.ui.lineEdit_2.text())


class StopDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = ui_StopDialog()
        self.ui.setupUi(self)

    @staticmethod
    def get_new(parent):
        dialog = StopDialog(parent)
        dialog.exec()
        if dialog.result() == QDialog.DialogCode.Rejected:
            return None
        return models.Stop(-1, dialog.ui.lineEdit.text(), True)


class DriverDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = ui_DriverDialog()
        self.ui.setupUi(self)

    @staticmethod
    def get_new(parent):
        dialog = DriverDialog(parent)
        dialog.exec()
        if dialog.result() == QDialog.DialogCode.Rejected:
            return None
        return models.Driver(-1, dialog.ui.lineEdit.text(), dialog.ui.lineEdit_2.text(), dialog.ui.lineEdit_3.text())


class ScheduleDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = ui_ScheduleDialog()
        self.ui.setupUi(self)
        self.ui.comboBox.insertItems(0, [f'{b.name} (остановок: {len(b.stops)})' for b in DB.get_routes()])

    @staticmethod
    def get_new(parent):
        dialog = ScheduleDialog(parent)
        dialog.exec()

        if dialog.result() == QDialog.DialogCode.Rejected:
            return None

        wd = []

        for cb in [
            dialog.ui.weekCheckBox_1,
            dialog.ui.weekCheckBox_2,
            dialog.ui.weekCheckBox_3,
            dialog.ui.weekCheckBox_4,
            dialog.ui.weekCheckBox_5,
            dialog.ui.weekCheckBox_6,
            dialog.ui.weekCheckBox_7
        ]:
            if cb.isChecked():
                wd.append(cb.text())

        return models.Schedule(-1,
                               dialog.ui.timeEdit.time().toPython(),
                               ", ".join(wd),
                               DB.get_routes()[dialog.ui.comboBox.currentIndex()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')

    window_1 = BusDialog(None)
    window_1.show()

    window_2 = DriverDialog(None)
    window_2.show()

    sys.exit(app.exec())
