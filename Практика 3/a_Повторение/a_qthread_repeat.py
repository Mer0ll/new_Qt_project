"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initTimer(1000)
        self.initSignals()

    def initUi(self):
        self.line_1 = QtWidgets.QLineEdit()
        self.line_1.setPlaceholderText('Некий текст')
        # self.button1 = QtWidgets.QPushButton('Старт!')
        self.button2 = QtWidgets.QPushButton('Очистить')
        self.layout1 = QtWidgets.QHBoxLayout()
        self.layout1.addWidget(self.line_1)
        # self.layout1.addWidget(self.button1)
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setValue(10)
        self.textP = QtWidgets.QPlainTextEdit()
        self.mainlayout = QtWidgets.QVBoxLayout()
        self.mainlayout.addLayout(self.layout1)
        self.mainlayout.addWidget(self.spinBox)
        self.mainlayout.addWidget(self.textP)
        self.mainlayout.addWidget(self.button2)

        self.setLayout(self.mainlayout)

    def initTimer(self, param):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(param)
        self.timer.start()

    def initSignals(self):
        self.button2.clicked.connect(self.textP.clear)
        # self.button1.clicked.connect(self.startGen)
        self.spinBox.textChanged.connect(self.setTimer)
        self.timer.timeout.connect(self.setTextEdit)

    def setTimer(self):
        data_spin = int(self.spinBox.text())
        self.timer.setInterval((data_spin + 1) * 100)

    # def startGen(self):
    #     self.gen = (val for val in self.text.text())

    @QtCore.Slot()
    def setTextEdit(self):
        data = self.line_1.text()
        if len(data) > 1:
            self.textP.appendPlainText(data[0])
            self.line_1.setText(data[1:])
        elif len(data) == 1:
            self.textP.appendPlainText(data)

        # try:
        #     self.textP.appendPlainText(next(self.gen))
        # except (StopIteration, TypeError):
        #     self.textP.setPlainText('Ahtung!')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
