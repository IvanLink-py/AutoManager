# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScheduleDialogXHkIII.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(399, 296)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.timeEdit = QTimeEdit(Dialog)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(100, 0))
        self.timeEdit.setTime(QTime(8, 0, 0))

        self.horizontalLayout_2.addWidget(self.timeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.weekCheckBox_1 = QCheckBox(Dialog)
        self.weekCheckBox_1.setObjectName(u"weekCheckBox_1")

        self.gridLayout.addWidget(self.weekCheckBox_1, 0, 0, 1, 1)

        self.weekCheckBox_6 = QCheckBox(Dialog)
        self.weekCheckBox_6.setObjectName(u"weekCheckBox_6")

        self.gridLayout.addWidget(self.weekCheckBox_6, 0, 1, 1, 1)

        self.weekCheckBox_2 = QCheckBox(Dialog)
        self.weekCheckBox_2.setObjectName(u"weekCheckBox_2")

        self.gridLayout.addWidget(self.weekCheckBox_2, 1, 0, 1, 1)

        self.weekCheckBox_7 = QCheckBox(Dialog)
        self.weekCheckBox_7.setObjectName(u"weekCheckBox_7")

        self.gridLayout.addWidget(self.weekCheckBox_7, 1, 1, 1, 1)

        self.weekCheckBox_3 = QCheckBox(Dialog)
        self.weekCheckBox_3.setObjectName(u"weekCheckBox_3")

        self.gridLayout.addWidget(self.weekCheckBox_3, 2, 0, 1, 1)

        self.weekCheckBox_4 = QCheckBox(Dialog)
        self.weekCheckBox_4.setObjectName(u"weekCheckBox_4")

        self.gridLayout.addWidget(self.weekCheckBox_4, 3, 0, 1, 1)

        self.weekCheckBox_5 = QCheckBox(Dialog)
        self.weekCheckBox_5.setObjectName(u"weekCheckBox_5")

        self.gridLayout.addWidget(self.weekCheckBox_5, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u043e\u0435 \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442", None))
        self.weekCheckBox_1.setText(QCoreApplication.translate("Dialog", u"\u041f\u043d", None))
        self.weekCheckBox_6.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431", None))
        self.weekCheckBox_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u0442", None))
        self.weekCheckBox_7.setText(QCoreApplication.translate("Dialog", u"\u0412\u0441", None))
        self.weekCheckBox_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u0440", None))
        self.weekCheckBox_4.setText(QCoreApplication.translate("Dialog", u"\u0427\u0442", None))
        self.weekCheckBox_5.setText(QCoreApplication.translate("Dialog", u"\u041f\u0442", None))
    # retranslateUi

