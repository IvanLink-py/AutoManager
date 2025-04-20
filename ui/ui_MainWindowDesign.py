# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowDesignZucvGT.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 770)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.addDriverAction = QAction(MainWindow)
        self.addDriverAction.setObjectName(u"addDriverAction")
        self.addBusAction = QAction(MainWindow)
        self.addBusAction.setObjectName(u"addBusAction")
        self.tripRepportAction = QAction(MainWindow)
        self.tripRepportAction.setObjectName(u"tripRepportAction")
        self.busDriverReportAction = QAction(MainWindow)
        self.busDriverReportAction.setObjectName(u"busDriverReportAction")
        self.addStopAction = QAction(MainWindow)
        self.addStopAction.setObjectName(u"addStopAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")

        self.verticalLayout_7.addWidget(self.label)

        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_3.setHandleWidth(15)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.routesListWidget = QListWidget(self.layoutWidget)
        self.routesListWidget.setObjectName(u"routesListWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.routesListWidget.sizePolicy().hasHeightForWidth())
        self.routesListWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.routesListWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.changeRoutePushButton = QPushButton(self.layoutWidget)
        self.changeRoutePushButton.setObjectName(u"changeRoutePushButton")

        self.horizontalLayout.addWidget(self.changeRoutePushButton)

        self.deleteRoutePushButton = QPushButton(self.layoutWidget)
        self.deleteRoutePushButton.setObjectName(u"deleteRoutePushButton")

        self.horizontalLayout.addWidget(self.deleteRoutePushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.splitter_2.addWidget(self.layoutWidget)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.routeNameLineEdit = QLineEdit(self.groupBox)
        self.routeNameLineEdit.setObjectName(u"routeNameLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.routeNameLineEdit.sizePolicy().hasHeightForWidth())
        self.routeNameLineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.routeNameLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.routeStopsListWidget = QListWidget(self.groupBox_2)
        self.routeStopsListWidget.setObjectName(u"routeStopsListWidget")
        sizePolicy.setHeightForWidth(self.routeStopsListWidget.sizePolicy().hasHeightForWidth())
        self.routeStopsListWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.routeStopsListWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.newRouteStopComboBox = QComboBox(self.groupBox_2)
        self.newRouteStopComboBox.setObjectName(u"newRouteStopComboBox")
        sizePolicy1.setHeightForWidth(self.newRouteStopComboBox.sizePolicy().hasHeightForWidth())
        self.newRouteStopComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.newRouteStopComboBox)

        self.addRouteStopPushButton = QPushButton(self.groupBox_2)
        self.addRouteStopPushButton.setObjectName(u"addRouteStopPushButton")
        self.addRouteStopPushButton.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_4.addWidget(self.addRouteStopPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.cancelPushButton = QPushButton(self.groupBox)
        self.cancelPushButton.setObjectName(u"cancelPushButton")

        self.horizontalLayout_2.addWidget(self.cancelPushButton)

        self.savePushButton = QPushButton(self.groupBox)
        self.savePushButton.setObjectName(u"savePushButton")

        self.horizontalLayout_2.addWidget(self.savePushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.splitter_2.addWidget(self.groupBox)
        self.splitter_3.addWidget(self.splitter_2)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.scheduleTableWidget = QTableWidget(self.splitter)
        if (self.scheduleTableWidget.columnCount() < 3):
            self.scheduleTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.scheduleTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.scheduleTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.scheduleTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.scheduleTableWidget.setObjectName(u"scheduleTableWidget")
        self.scheduleTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.scheduleTableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.scheduleTableWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.scheduleTableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.splitter.addWidget(self.scheduleTableWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(120, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.groupBox_3 = QGroupBox(self.layoutWidget1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.nextScheduleListWidget = QListWidget(self.groupBox_3)
        self.nextScheduleListWidget.setObjectName(u"nextScheduleListWidget")

        self.verticalLayout_5.addWidget(self.nextScheduleListWidget)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.busComboBox = QComboBox(self.groupBox_3)
        self.busComboBox.setObjectName(u"busComboBox")

        self.horizontalLayout_6.addWidget(self.busComboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.driverComboBox = QComboBox(self.groupBox_3)
        self.driverComboBox.setObjectName(u"driverComboBox")

        self.horizontalLayout_5.addWidget(self.driverComboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.sendPushButton = QPushButton(self.groupBox_3)
        self.sendPushButton.setObjectName(u"sendPushButton")

        self.verticalLayout_5.addWidget(self.sendPushButton)


        self.horizontalLayout_7.addWidget(self.groupBox_3)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(120, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.groupBox_4 = QGroupBox(self.layoutWidget_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.currentTripListWidget = QListWidget(self.groupBox_4)
        self.currentTripListWidget.setObjectName(u"currentTripListWidget")

        self.verticalLayout_6.addWidget(self.currentTripListWidget)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.tripStatusComboBox = QComboBox(self.groupBox_4)
        self.tripStatusComboBox.addItem("")
        self.tripStatusComboBox.addItem("")
        self.tripStatusComboBox.setObjectName(u"tripStatusComboBox")

        self.horizontalLayout_10.addWidget(self.tripStatusComboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.endTripPushButton = QPushButton(self.groupBox_4)
        self.endTripPushButton.setObjectName(u"endTripPushButton")

        self.verticalLayout_6.addWidget(self.endTripPushButton)


        self.horizontalLayout_8.addWidget(self.groupBox_4)

        self.splitter.addWidget(self.layoutWidget_2)
        self.splitter_3.addWidget(self.splitter)

        self.verticalLayout_7.addWidget(self.splitter_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1146, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.addDriverAction)
        self.menu.addAction(self.addBusAction)
        self.menu.addAction(self.addStopAction)
        self.menu_2.addAction(self.tripRepportAction)
        self.menu_2.addAction(self.busDriverReportAction)
        self.menu_3.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.addDriverAction.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.addBusAction.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u0432\u0442\u043e\u0431\u0443\u0441", None))
        self.tripRepportAction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0451\u0442 \u043f\u043e \u0440\u0435\u0439\u0441\u0430\u043c", None))
        self.busDriverReportAction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442 \u043f\u043e \u0430\u0432\u0442\u043e\u0431\u0443\u0441\u0430\u043c \u0438 \u0432\u043e\u0434\u0435\u043b\u044f\u043c", None))
        self.addStopAction.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421 \u0430\u0432\u0442\u043e\u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0433\u043e \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.changeRoutePushButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.deleteRoutePushButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.addRouteStopPushButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.cancelPushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.scheduleTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442", None));
        ___qtablewidgetitem1 = self.scheduleTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem2 = self.scheduleTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043d\u0438 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u043e\u0442\u043f\u0440\u0430\u043b\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0431\u0443\u0441", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.sendPushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0440\u0435\u0439\u0441\u044b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.tripStatusComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043f\u0435\u0448\u043d\u043e", None))
        self.tripStatusComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u044b\u0432 \u0440\u0435\u0439\u0441\u0430", None))

        self.endTripPushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

