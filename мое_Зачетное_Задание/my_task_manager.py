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
        match self.flag:
            case 'Монитор ресурсов':
                self.openResourceMonitor()
            case 'Запущенные процессы' | 'Службы' | 'Планировщик задач':
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
        uname = platform.uname()
        # cpufreg = psutil.cpu_freq()
        svmem = psutil.virtual_memory()
        cpufreg = psutil.cpu_freq()

        while True:
            name_processor = uname.processor.split()[0]  # Процессор
            cpu_logic = psutil.cpu_count(logical=True)  # Всего ядер
            cpu_fisic = psutil.cpu_count(logical=False)  # Физические ядра
            cpu_max = cpufreg.max  # Максимальная частота
            currentfreq = cpufreg.current  # Текущая частота
            totalCPUusage = psutil.cpu_percent()  # Общая загруженность процессора
            cpufregmax = cpufreg.max  # Максимальная частота
            # cpufregmin = cpufreg.min  # Минимальная частота

            ramsize = self.get_size(svmem.total)  # Объем Ram
            avaram = self.get_size(svmem.available)  # Доступно Ram
            usedram = self.get_size(svmem.used)  # Используется Ram
            percentram = svmem.percent  # Процент
            fullcpu_percent = psutil.cpu_percent(percpu=True, interval=1)

            self.workerCPU.emit([name_processor,
                                 cpu_logic,
                                 cpu_fisic,
                                 cpu_max,
                                 currentfreq,
                                 totalCPUusage,
                                 cpufregmax,
                                 ramsize,
                                 avaram,
                                 usedram,
                                 usedram,
                                 percentram,
                                 fullcpu_percent
                                 ])
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
        self.initThread()
        self.initProgresBar()
        self.initRAmInfo()
        self.initSignal()

    def initThread(self):
        self.thread1 = WorkerRM()
        self.thread1.workerCPU.connect(self.reportCPU)
        self.thread1.start()

    def initProgresBar(self):
        layout_dynamic = QtWidgets.QVBoxLayout()
        self.bar_list = []
        for core, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1), 1):
            sup_layout = QtWidgets.QHBoxLayout()
            label_dunamic = QtWidgets.QLabel(f'Ядро {core}:')
            progressbar_dunamic = QtWidgets.QProgressBar()
            self.bar_list.append(progressbar_dunamic)
            progressbar_dunamic.setValue(percentage)
            sup_layout.addWidget(label_dunamic)
            sup_layout.addWidget(progressbar_dunamic)
            layout_dynamic.addLayout(sup_layout)
        sup_layout = QtWidgets.QHBoxLayout()
        label_dunamic = QtWidgets.QLabel(f'Общая загруженность процессора: ')
        percent = psutil.cpu_percent()
        progressbar_dunamic = QtWidgets.QProgressBar()
        self.bar_list.append(progressbar_dunamic)
        progressbar_dunamic.setValue(percent)
        sup_layout.addWidget(label_dunamic)
        sup_layout.addWidget(progressbar_dunamic)
        layout_dynamic.addLayout(sup_layout)

        self.ui.verticalLayout.addLayout(layout_dynamic)

    def reportCPU(self, s):
        self.ui.lineEdit_4.setText(s[0])  # Процессор
        self.ui.lineEdit.setText(f'{s[1]}')  # Всего ядер
        self.ui.lineEdit_2.setText(f'{s[2]}')  # Физические ядра
        self.ui.lineEdit_3.setText(f'{s[3]:.2f} МГц')  # Максимальная частота
        self.ui.lineEdit_5.setText(f'{s[4]:.2f} МГц')  # Максимальная частота
        for corre in range(len(s[-1])):
            self.bar_list[corre].setValue(s[-1][corre])
        self.bar_list[-1].setValue(s[5])
        self.ui.lineEdit_6.setText(s[7])
        self.ui.lineEdit_8.setText(s[8])
        self.ui.lineEdit_7.setText(s[9])
        self.ui.progressBar.setValue(s[-2])

    def initRAmInfo(self):
        partitions = psutil.disk_partitions()
        disk_info_layout = QtWidgets.QVBoxLayout()
        for partition in partitions:
            disk_lable = QtWidgets.QLabel(f'=== Диск: {partition.device}')
            disk_info_layout.addWidget(disk_lable)
            type_disk = QtWidgets.QLabel(f' Тип файловой системы: {partition.fstype}')
            disk_info_layout.addWidget(type_disk)
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                break
            total_usage_disk = QtWidgets.QLabel(f'    Общий объем: {WorkerRM.get_size(partition_usage.total)}')
            disk_info_layout.addWidget(total_usage_disk)
            used_usage = QtWidgets.QLabel(f'    Используется: {WorkerRM.get_size(partition_usage.used)}')
            disk_info_layout.addWidget(used_usage)
            usage_free = QtWidgets.QLabel(f'    Свободно: {WorkerRM.get_size(partition_usage.free)}')
            disk_info_layout.addWidget(usage_free)
            usage_percent = QtWidgets.QLabel(f'    Процент: {partition_usage.percent} %')
            disk_info_layout.addWidget(usage_percent)

        self.ui.groupBox_4.setLayout(disk_info_layout)

    def initSignal(self):
        self.ui.spinBox.valueChanged.connect(self.InfoDelay)
        self.thread1.finished.connect(self.thread1.deleteLater)

    def InfoDelay(self):
        self.thread1.delay = self.ui.spinBox.value()


if __name__ == '__main__':
    main()
