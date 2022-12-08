"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

import time

import requests
from PySide6 import QtWidgets, QtCore


class Worker(QtCore.QThread):
    progress = QtCore.Signal(int)
    url = None

    def start(self, *args, url=None, **kwargs):
        self.url = url
        return super().start(*args, **kwargs)

    def run(self) -> None:
        """
        Метод имитирующий долгую задачу

        :return: None
        """

        data = requests.get(self.url)
        self.progress.emit(data.status_code)
        self.finished.emit()


class Window(QtWidgets.QWidget):
    class Window(QtWidgets.QWidget):

        def __init__(self, parent=None):
            super().__init__(parent)
            self.initUi()
            self.initSignals()
            self.initTread()


        def initUi(self):
            self.line_1 = QtWidgets.QLineEdit()
            self.line_1.setPlaceholderText('Адрес')
            self.button1 = QtWidgets.QPushButton('Проверить!')
            self.button2 = QtWidgets.QPushButton('Очистить!')
            self.layout1 = QtWidgets.QHBoxLayout()
            self.layout1.addWidget(self.line_1)
            self.layout1.addWidget(self.button1)
            self.textP = QtWidgets.QPlainTextEdit()
            self.mainlayout = QtWidgets.QVBoxLayout()
            self.mainlayout.addLayout(self.layout1)
            self.mainlayout.addWidget(self.textP)
            self.mainlayout.addWidget(self.button2)

            self.setLayout(self.mainlayout)

        def initSignals(self):
            self.button1.clicked.connect(self.startProcess)
            self.button2.clicked.connect(self.textP.clear)

            self.thread.progress.connect(self.reportProgress)
            self.thread.finished.connect(lambda: self.button1.setEnabled(True))
            self.thread.finished.connect(self.thread.quit)

        def initTread(self):
            self.thread = Worker()

        @QtCore.Slot()
        def startProcess(self):
            self.button1.setEnabled(False)
            self.thread.start(url=self.line_1.text())

        @QtCore.Slot()
        def reportProgress(self, progres):
            self.textP.appendPlainText(str(progres))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
