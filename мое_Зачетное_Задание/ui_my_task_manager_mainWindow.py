# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_my_task_manager_mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        if not mainForm.objectName():
            mainForm.setObjectName(u"mainForm")
        mainForm.resize(270, 310)
        font = QFont()
        font.setPointSize(10)
        mainForm.setFont(font)
        mainForm.setFocusPolicy(Qt.NoFocus)
        self.verticalLayout_3 = QVBoxLayout(mainForm)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(mainForm)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        self.label_3.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setFont(font2)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setFont(font2)
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font2)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.pushButton.setFont(font3)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.retranslateUi(mainForm)

        QMetaObject.connectSlotsByName(mainForm)
    # setupUi

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(QCoreApplication.translate("mainForm", u"\u0414\u0438\u0441\u043f\u0435\u0442\u0447\u0435\u0440", None))
        self.groupBox.setTitle(QCoreApplication.translate("mainForm", u"\u041e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.label_3.setText(QCoreApplication.translate("mainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b:", None))
        self.label_4.setText(QCoreApplication.translate("mainForm", u"\u0418\u043c\u044f \u0443\u0437\u043b\u0430:", None))
        self.label.setText(QCoreApplication.translate("mainForm", u"\u0412\u044b\u043f\u0443\u0441\u043a:", None))
        self.label_5.setText(QCoreApplication.translate("mainForm", u"\u0412\u0435\u0440\u0441\u0438\u044f:", None))
        self.label_2.setText(QCoreApplication.translate("mainForm", u"\u041c\u0430\u0448\u0438\u043d\u0430:", None))
        self.pushButton.setText(QCoreApplication.translate("mainForm", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

