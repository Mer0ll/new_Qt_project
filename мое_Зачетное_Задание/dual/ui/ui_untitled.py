# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(565, 470)
        self.verticalLayout_12 = QVBoxLayout(Form)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.spinBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_13 = QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMouseTracking(False)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMouseTracking(False)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy1.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy1)
        self.lineEdit_4.setMouseTracking(False)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy1)
        self.lineEdit_5.setMouseTracking(False)
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lineEdit_5)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy1.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy1)
        self.lineEdit_6.setMouseTracking(False)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy1.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy1)
        self.lineEdit_7.setMouseTracking(False)
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.lineEdit_8 = QLineEdit(self.groupBox_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy1.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy1)
        self.lineEdit_8.setMouseTracking(False)
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lineEdit_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(self.groupBox_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy1.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy1)
        self.lineEdit_9.setMouseTracking(False)
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lineEdit_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.lineEdit_10 = QLineEdit(self.groupBox_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy1.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy1)
        self.lineEdit_10.setMouseTracking(False)
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_5.addWidget(self.groupBox_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.lineEdit_11 = QLineEdit(self.groupBox_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy1.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy1)
        self.lineEdit_11.setMouseTracking(False)
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lineEdit_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.lineEdit_12 = QLineEdit(self.groupBox_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy1.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy1)
        self.lineEdit_12.setMouseTracking(False)
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lineEdit_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_16.addWidget(self.label_14)

        self.lineEdit_13 = QLineEdit(self.groupBox_3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy1.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy1)
        self.lineEdit_13.setMouseTracking(False)
        self.lineEdit_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lineEdit_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout_18.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_8_dunamic = QVBoxLayout()
        self.verticalLayout_8_dunamic.setObjectName(u"verticalLayout_8_dunamic")

        self.verticalLayout_7.addLayout(self.verticalLayout_8_dunamic)


        self.horizontalLayout_18.addWidget(self.groupBox_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)


        self.verticalLayout_13.addLayout(self.verticalLayout_9)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_8.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_11 = QVBoxLayout(self.tab_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tableWidget_2 = QTableWidget(self.tab_3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_11.addWidget(self.tableWidget_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_20 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.tableWidget_3 = QTableWidget(self.tab_4)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.horizontalLayout_20.addWidget(self.tableWidget_3)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_10.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u043f\u0435\u0442\u0447\u0435\u0440", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u043b\u044f\u0442\u044c \u043a\u0430\u0436\u0434\u044b\u0435, \u0441\u0435\u043a:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0443\u0437\u043b\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u043f\u0443\u0441\u043a:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u0441\u0438\u044f:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u0448\u0438\u043d\u0430:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0435", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0424\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u044f\u0434\u0440\u0430:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u0435\u0433\u043e \u044f\u0434\u0435\u0440:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u044f\u043c\u044f\u0442\u0438", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044c\u0435\u043c:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0434\u0438\u0441\u043a\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u041c\u043e\u043d\u0438\u0442\u043e\u0440 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0449\u0435\u043d\u043d\u044b\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u0421\u043b\u0443\u0436\u0431\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a \u0437\u0430\u0434\u0430\u0447", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

