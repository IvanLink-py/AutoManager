import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_MainWindowDesign import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('fusion')

    window = MainWindow()
    window.show()

    sys.exit(app.exec())