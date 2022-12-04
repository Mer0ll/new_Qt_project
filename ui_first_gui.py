# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_first_gui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(506, 101)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_1 = QLineEdit(Form)
        self.input_1.setObjectName(u"input_1")
        self.input_1.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_1.sizePolicy().hasHeightForWidth())
        self.input_1.setSizePolicy(sizePolicy)
        self.input_1.setAlignment(Qt.AlignCenter)
        self.input_1.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.input_1)

        self.output_2 = QLineEdit(Form)
        self.output_2.setObjectName(u"output_2")
        self.output_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.output_2.setEchoMode(QLineEdit.NoEcho)
        self.output_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.output_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u0432\u0435\u0442 ;)", None))
        self.input_1.setInputMask("")
        self.input_1.setPlaceholderText(QCoreApplication.translate("Form", u"InPut", None))
        self.output_2.setInputMask("")
        self.output_2.setText("")
        self.output_2.setPlaceholderText(QCoreApplication.translate("Form", u"OutPut", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u0432\u0435\u0440\u043d\u0438!", None))
    # retranslateUi

