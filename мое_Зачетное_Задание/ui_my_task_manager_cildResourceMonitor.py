# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_my_task_manager_cildResourceMonitor.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(1100, 590)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setBaseSize(QSize(1100, 800))
        self.verticalLayout_17 = QVBoxLayout(Form)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font3 = QFont()
        font3.setBold(True)
        self.groupBox_2.setFont(font3)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setBold(False)
        self.label_3.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_3.addWidget(self.label_8)

        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.progressBar_2 = QProgressBar(self.groupBox_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)

        self.horizontalLayout_3.addWidget(self.progressBar_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_11)

        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_12)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_13)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit_6 = QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.groupBox_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.groupBox_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lineEdit_9)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_9.addWidget(self.label_14)

        self.progressBar_3 = QProgressBar(self.groupBox_4)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(24)

        self.verticalLayout_9.addWidget(self.progressBar_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.verticalLayout_13.addLayout(self.verticalLayout_10)


        self.horizontalLayout_9.addWidget(self.groupBox_4)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font3)
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_15)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_16)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_17)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_18)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_19)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lineEdit_10 = QLineEdit(self.groupBox_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.groupBox_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.groupBox_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lineEdit_12)

        self.lineEdit_14 = QLineEdit(self.groupBox_3)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.groupBox_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lineEdit_15)


        self.horizontalLayout_7.addLayout(self.verticalLayout_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)
        self.label_20.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_6.addWidget(self.label_20)

        self.progressBar_4 = QProgressBar(self.groupBox_3)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setValue(24)

        self.verticalLayout_6.addWidget(self.progressBar_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_15.addWidget(self.groupBox_3)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_16.addWidget(self.pushButton)


        self.verticalLayout_17.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        Form.setWindowFlags(Qt.FramelessWindowHint)
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041c\u043e\u043d\u0438\u0442\u043e\u0440 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0426\u041f:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"CPU", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u0435\u0433\u043e \u044f\u0434\u0435\u0440:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0424\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u044f\u0434\u0440\u0430:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0430\u044f \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u044f\u0434\u0440\u0430:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Ram", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044a\u0435\u043c \u043f\u0430\u043c\u044f\u0442\u0438:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e \u043f\u0430\u043c\u044f\u0442\u0438:", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Disck", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u043a:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u0444\u0430\u0439\u043b\u043e\u0432\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0438\u0439 \u043e\u0431\u044a\u0435\u043c:", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f:", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u043e:", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

