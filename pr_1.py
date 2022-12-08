# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pr_1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1096, 869)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1076, 808))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(386, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_3.addWidget(self.checkBox_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.groupBox_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.toolBox = QToolBox(self.tab)
        self.toolBox.setObjectName(u"toolBox")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 513, 605))
        self.verticalLayout_7 = QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.page_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.page_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lineEdit_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.page_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lineEdit_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lineEdit_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 472, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_3, u"QLineEdit")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_6 = QHBoxLayout(self.page_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textEdit = QTextEdit(self.page_5)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_6.addWidget(self.textEdit)

        self.toolBox.addItem(self.page_5, u"QTextEdit")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_8 = QVBoxLayout(self.page_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.plainTextEdit = QPlainTextEdit(self.page_6)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_8.addWidget(self.plainTextEdit)

        self.toolBox.addItem(self.page_6, u"QPlaineTextEdit")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 513, 605))
        self.horizontalLayout_11 = QHBoxLayout(self.page_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.calendarWidget = QCalendarWidget(self.page_4)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.horizontalLayout_11.addWidget(self.calendarWidget)

        self.verticalSpacer = QSpacerItem(20, 584, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_11.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page_4, u"QCalenderWidget")

        self.horizontalLayout_5.addWidget(self.toolBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_1 = QPushButton(self.tab)
        self.pushButton_1.setObjectName(u"pushButton_1")
        font = QFont()
        font.setPointSize(8)
        self.pushButton_1.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(740, 70, 221, 241))
        font1 = QFont()
        font1.setPointSize(10)
        self.groupBox_3.setFont(font1)
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.progressBar = QProgressBar(self.groupBox_3)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setValue(10)
        self.progressBar.setOrientation(Qt.Vertical)

        self.verticalLayout_6.addWidget(self.progressBar)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"line_1")

        self.verticalLayout_6.addWidget(self.label)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.progressBar_2 = QProgressBar(self.groupBox_3)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setValue(50)
        self.progressBar_2.setOrientation(Qt.Vertical)

        self.verticalLayout_9.addWidget(self.progressBar_2)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.progressBar_3 = QProgressBar(self.groupBox_3)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy)
        self.progressBar_3.setValue(100)
        self.progressBar_3.setOrientation(Qt.Vertical)

        self.verticalLayout_10.addWidget(self.progressBar_3)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)


        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.tableView = QTableView(self.tab_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(690, 460, 256, 192))
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(4, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(5, 5, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 40, 691, 211))
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1096, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"QRadioButtom", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton_1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton_2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton_3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"QCheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"QLineEdit", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">123456789</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"QTextEdit", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0412\u0430\u0448\u0430 \u0440\u0435\u043a\u043b\u0430\u043c\u0430 ;))", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"QPlaineTextEdit", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"QCalenderWidget", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem15 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem16 = self.tableWidget.item(4, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem17 = self.tableWidget.item(5, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"6", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

