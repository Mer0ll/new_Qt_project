# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_my_task_manager_cildRunningProcesses.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 800)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.groupBox)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        Form.setWindowFlags(Qt.FramelessWindowHint)
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0449\u0435\u043d\u043d\u044b\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

