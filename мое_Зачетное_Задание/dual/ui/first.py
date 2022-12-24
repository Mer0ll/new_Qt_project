import platform
import time

import psutil
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import (QSizePolicy)

from ui_untitled import Ui_Form


def main():
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()


class WorkerMemoryInfo(QtCore.QThread):
    WorkerMI = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent()  # загрузку CPU
            ram_value = psutil.virtual_memory().percent  # получите загрузку RAM
            self.WorkerMI.emit(
                [cpu_value, ram_value])
            time.sleep(self.delay)
        self.finished.emit()


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initThreads()
        self.initSignals()
        # self.getpids()
        self.iniLibraries()
        self.resourceMonitor()
        self.processorInfo()
        self.memoryInfo()

    def iniLibraries(self):
        self.uname = platform.uname()
        self.cpufreg = psutil.cpu_freq()
        self.svmem = psutil.virtual_memory()

    @staticmethod
    def get_size(bytes, suffix='B'):
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < factor:
                return f'{bytes:.2f}{unit}{suffix}'
            bytes /= factor

    def initThreads(self):
        self.thread1 = WorkerMemoryInfo()
        self.thread1.WorkerMI.connect(self.progressBars)
        self.thread1.start()

    def getpids(self):
        ps = psutil.pids()
        self.ui.tableWidget.setColumnCount(3)  # создал один столбец
        self.ui.tableWidget.setRowCount(len(ps))  # сразу создал необходимое кол-во строк

        self.ui.tableWidget.setHorizontalHeaderLabels(['Pid', 'Name', 'Status'])  # установил заголовок столбца

        for i in range(len(ps)):
            proces = psutil.Process(ps[i])
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(f'{ps[i]}'))  # заполнил pid
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(f'{proces.name()}'))  # заполнил имя процесса
            self.ui.tableWidget.setItem(i, 2,
                                        QtWidgets.QTableWidgetItem(f'{proces.status()}'))  # заполнил статус процесса

        self.ui.tableWidget.resizeColumnsToContents()

    def resourceMonitor(self):
        self.ui.lineEdit.setText(self.uname.system)
        self.ui.lineEdit_2.setText(self.uname.node)
        self.ui.lineEdit_3.setText(self.uname.release)
        self.ui.lineEdit_4.setText(self.uname.version)
        self.ui.lineEdit_5.setText(self.uname.machine)

    def processorInfo(self):
        self.ui.lineEdit_6.setText(f'{self.uname.processor.split()[0]}')
        self.ui.lineEdit_7.setText(f'{self.cpufreg.max:.2f}МГц')
        self.ui.lineEdit_8.setText(f'{psutil.cpu_count(logical=True)}')
        self.ui.lineEdit_9.setText(f'{psutil.cpu_count(logical=False)}')
        self.barProgress_RAM = QtWidgets.QProgressBar()
        sizePolicyRam = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicyRam.setHorizontalStretch(0)
        sizePolicyRam.setVerticalStretch(0)
        sizePolicyRam.setHeightForWidth(self.barProgress_RAM.sizePolicy().hasHeightForWidth())
        self.barProgress_RAM.setSizePolicy(sizePolicyRam)
        self.ui.verticalLayout_3.addWidget(self.barProgress_RAM)

    def memoryInfo(self):
        self.ui.lineEdit_11.setText(f'{self.get_size(self.svmem.total)}')
        self.ui.lineEdit_12.setText(f'{self.get_size(self.svmem.available)}')
        self.ui.lineEdit_13.setText(f'{self.get_size(self.svmem.used)}')
        self.barProgress = QtWidgets.QProgressBar()
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.barProgress.sizePolicy().hasHeightForWidth())
        self.barProgress.setSizePolicy(sizePolicy1)
        self.ui.verticalLayout_6.addWidget(self.barProgress)

    def progressBars(self, report):
        self.ui.lineEdit_10.setText(f'{report[0]:.2f}МГц')
        self.barProgress_RAM.setValue(report[0])
        self.barProgress.setValue(report[1])

    def initSignals(self):
        self.ui.spinBox.valueChanged.connect(self.setupdate)
        self.thread1.finished.connect(self.thread1.deleteLater)

    def setupdate(self):
        self.thread1.delay = self.ui.spinBox.value()


if __name__ == '__main__':
    main()
