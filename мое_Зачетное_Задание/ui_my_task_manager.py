# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_my_task_manager.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QSizePolicy,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 760)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.tab_3)
        self.comboBox.setObjectName(u"comboBox")

        dialog_boxes = ['',
                        'Процессор, количество ядер, текущая загрузка',
                        'Оперативная памяти, загрузка',
                        'Информация о жестких дисках']

        self.comboBox.addItems(dialog_boxes)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.textEdit_4 = QTextEdit(self.tab_3)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.verticalLayout_2.addWidget(self.textEdit_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit_3 = QTextEdit(self.tab_4)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.horizontalLayout_3.addWidget(self.textEdit_3)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit_2 = QTextEdit(self.tab_6)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout = QVBoxLayout(self.tab_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.tab_5)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.tabWidget.addTab(self.tab_5, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u043f\u0435\u0442\u0447\u0435\u0440 \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u041e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u0421\u043b\u0443\u0436\u0431\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a \u0437\u0430\u0434\u0430\u0447", None))
    # retranslateUi

