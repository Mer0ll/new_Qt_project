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
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        if not mainForm.objectName():
            mainForm.setObjectName(u"mainForm")
        mainForm.resize(270, 310)
        font = QFont()
        font.setPointSize(10)
        mainForm.setFont(font)
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        self.comboBox.setFont(font3)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.retranslateUi(mainForm)

        QMetaObject.connectSlotsByName(mainForm)
    # setupUi

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(QCoreApplication.translate("mainForm", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("mainForm", u"\u041e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.label.setText(QCoreApplication.translate("mainForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b:", None))
        self.label_6.setText(QCoreApplication.translate("mainForm", u"0", None))
        self.label_2.setText(QCoreApplication.translate("mainForm", u"\u0418\u043c\u044f \u0443\u0437\u043b\u0430:", None))
        self.label_7.setText(QCoreApplication.translate("mainForm", u"0", None))
        self.label_3.setText(QCoreApplication.translate("mainForm", u"\u0412\u044b\u043f\u0443\u0441\u043a:", None))
        self.label_8.setText(QCoreApplication.translate("mainForm", u"0", None))
        self.label_4.setText(QCoreApplication.translate("mainForm", u"\u0412\u0435\u0440\u0441\u0438\u044f:", None))
        self.label_9.setText(QCoreApplication.translate("mainForm", u"0", None))
        self.label_5.setText(QCoreApplication.translate("mainForm", u"\u041c\u0430\u0448\u0438\u043d\u0430:", None))
        self.label_10.setText(QCoreApplication.translate("mainForm", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("mainForm", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

