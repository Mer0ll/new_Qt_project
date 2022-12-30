import platform
import subprocess
import time

import psutil
from PySide6 import QtWidgets, QtCore

from ui.ui_cildWindow import Ui_Form
from ui_my_task_manager_cildResourceMonitor2 import Ui_Form as UI_rm
from ui_my_task_manager_mainWindow import Ui_mainForm


def main():
    app = QtWidgets.QApplication()

    taskmanager = MainWindows()
    taskmanager.show()

    app.exec()


class MainWindows(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mainForm()
        self.ui.setupUi(self)
        self.flag = None
        combobox = ['',
                    'Монитор ресурсов',
                    'Запущенные процессы',
                    'Службы',
                    'Планировщик задач']
        self.ui.comboBox.addItems(combobox)
        self.setAboutSystem()
        self.initSignals()

    def setAboutSystem(self):
        uname = platform.uname()
        self.ui.lineEdit_3.setText(uname.system)  # Система
        self.ui.lineEdit_4.setText(uname.node)  # Имя узла
        self.ui.lineEdit.setText(uname.release)  # Выпуск
        self.ui.lineEdit_5.setText(uname.version)  # Версия
        self.ui.lineEdit_2.setText(uname.machine)  # Машина

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.initChildWindow)

    def initChildWindow(self):
        self.flag = self.ui.comboBox.currentText()
        if self.flag == 'Монитор ресурсов':
            self.openResourceMonitor()
        if self.flag in ('Запущенные процессы', 'Службы', 'Планировщик задач'):
            self.openOpenChildWindow()

    def openOpenChildWindow(self):
        self.childWindow = ChildWindow(self.flag)
        self.childWindow.show()

    def openResourceMonitor(self):
        self.childWindow = ResourceMonitor()
        self.childWindow.show()


class WorkerRM(QtCore.QThread):
    workerCPU = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    @staticmethod
    def get_size(bytes, suffix='B'):
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < factor:
                return f'{bytes:.2f}{unit}{suffix}'
            bytes /= factor

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        cpufreg = psutil.cpu_freq()
        svmem = psutil.virtual_memory()
        while True:
            currentfreq = cpufreg.current  # Текущая частота
            totalCPUusage = psutil.cpu_percent()  # Общая загруженность процессора
            cpufregmax = cpufreg.max  # Максимальная частота
            cpufregmin = cpufreg.min  # Минимальная частота

            ramsize = self.get_size(svmem.total)  # Объем Ram
            avaram = self.get_size(svmem.available)  # Доступно Ram
            usedram = self.get_size(svmem.used)  # Используется Ram
            percentram = svmem.percent  # Процент
            fullcpu_percent = psutil.cpu_percent(percpu=True, interval=1)

            self.workerCPU.emit([currentfreq,
                                 totalCPUusage,
                                 cpufregmax,
                                 cpufregmin,
                                 ramsize,
                                 avaram,
                                 usedram,
                                 usedram,
                                 percentram,
                                 fullcpu_percent])
            time.sleep(self.delay)
        self.finished.emit()


class ChildWindow(QtWidgets.QWidget):
    dict_gets = {'Запущенные процессы': 'Get-Process',
                 'Службы': 'Get-Service',
                 'Планировщик задач': 'Get-ScheduledTask'}

    def __init__(self, flag, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.flag = flag
        self.setTitl()
        pr = self.getRP()
        self.splitterRP(pr)

    def setTitl(self):
        self.setWindowTitle(self.flag)
        self.ui.groupBox.setTitle(self.flag)

    def getRP(self):
        return subprocess.check_output(
            f'powershell -Executionpolicy ByPass -Command {self.dict_gets[self.flag]}').decode(
            encoding='cp866')

    def splitterRP(self, string):
        b = string.strip().split('\r\n')
        headers = b[0].split()
        self.ui.tableWidget.setColumnCount(len(headers))  # создал столбецы
        self.ui.tableWidget.setRowCount(len(b) - 2)  # сразу создал необходимое кол-во строк
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)  # установил заголовок столбца
        for i in range(len(b[2:])):
            elem = b[2:][i].split()
            if len(elem) < len(headers) and self.flag == 'Запущенные процессы':
                elem.insert(4, f'{0:.2f}')
            for j in range(len(headers)):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(f'{elem[j]}'))

        self.ui.tableWidget.resizeColumnsToContents()


class ResourceMonitor(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UI_rm()
        self.ui.setupUi(self)
        self.setCPUInfo()
        # self.initThread()
        # self.startThread()
        # self.initSignals()

    def setCPUInfo(self):
        uname = platform.uname()
        cpufreg = psutil.cpu_freq()
        self.ui.lineEdit_4.setText(uname.processor.split()[0])  # Процессор
        self.ui.lineEdit.setText(f'{psutil.cpu_count(logical=True)}')  # Всего ядер
        self.ui.lineEdit_2.setText(f'{psutil.cpu_count(logical=False)}')  # Физические ядра
        self.ui.lineEdit_3.setText(f'{cpufreg.max:.2f} МГц')
        layout_dynamic = QtWidgets.QVBoxLayout()
        for core, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            label_dunamic = QtWidgets.QLabel(f'Ядро {core}: {percentage} %')
        #     layout_dynamic.addWidget(label_dunamic)
        #     # print(f'Ядро {core}: {percentage} %')
        # self.ui.horizontalLayout_3.addLayout(layout_dynamic)

    def initSignals(self):
        self.thread1.workerCPU.connect(self.reportCPU)

        self.thread1.finished.connect(self.thread1.deleteLater)

    def initThread(self):
        self.thread1 = WorkerRM()

    def startThread(self):
        self.thread1.start()

    def reportCPU(self, s):
        ...


if __name__ == '__main__':
    main()
