import platform
import subprocess
import time

import psutil
from PySide6 import QtWidgets, QtCore

from ui_my_task_manager_cildManagerTask import Ui_Form as UI_ManagerTask
from ui_my_task_manager_cildResourceMonitor import Ui_Form as UI_rm
from ui_my_task_manager_cildRunningProcesses import Ui_Form as UI_RunningProcesses
from ui_my_task_manager_cildWindowServices import Ui_Form as UI_Service
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
        self.ui.label_6.setText(uname.system)  # Система
        self.ui.label_7.setText(uname.node)  # Имя узла
        self.ui.label_8.setText(uname.release)  # Выпуск
        self.ui.label_9.setText(uname.version)  # Версия
        self.ui.label_10.setText(uname.machine)  # Машина

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.openChildWindow)

    def openChildWindow(self):
        if self.ui.comboBox.currentText() == 'Монитор ресурсов':
            self.openResourceMonitor()
        elif self.ui.comboBox.currentText() == 'Запущенные процессы':
            self.openRunningProcesses()
        elif self.ui.comboBox.currentText() == 'Службы':
            self.openServices()
        elif self.ui.comboBox.currentText() == 'Планировщик задач':
            self.openManagerTask()

    def openResourceMonitor(self):
        self.cildWindowResourceMonitor = ResourceMonitor()
        self.cildWindowResourceMonitor.show()

    def openRunningProcesses(self):
        self.cildWindowRunningProcesses = RunningProcesses()
        self.cildWindowRunningProcesses.show()

    def openServices(self):
        self.cildWindowServices = Services()
        self.cildWindowServices.show()

    def openManagerTask(self):
        self.cildWindowManagerTask = ManagerTask()
        self.cildWindowManagerTask.show()


class BaseWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initializationUi()
        self.ui.setupUi(self)
        self.initSignals()

    def initializationUi(self):
        self.ui = UI_RunningProcesses()

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()


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


class ResourceMonitor(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UI_rm()
        self.ui.setupUi(self)
        self.setCPUInfo()
        self.initThread()
        self.startThread()
        self.initSignals()

    def setCPUInfo(self):
        uname = platform.uname()
        self.ui.label_2.setText(uname.processor)  # Процессор
        self.ui.label_13.setText(f'{psutil.cpu_count(logical=True)}')  # Всего ядер
        self.ui.label_21.setText(f'{psutil.cpu_count(logical=False)}')  # Физические ядра
        layout_dynamic = QtWidgets.QVBoxLayout()
        for core, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            label_dunamic = QtWidgets.QLabel(f'Ядро {core}: {percentage} %')
            layout_dynamic.addWidget(label_dunamic)
            # print(f'Ядро {core}: {percentage} %')
        self.ui.horizontalLayout_3.addLayout(layout_dynamic)

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.closeWindow)
        self.thread1.workerCPU.connect(self.reportCPU)

        self.thread1.finished.connect(self.thread1.deleteLater)

    def closeWindow(self):
        self.close()

    def initThread(self):
        self.thread1 = WorkerRM()

    def startThread(self):
        self.thread1.start()

    def reportCPU(self, s):
        self.ui.label_22.setText(f'{s[2]:.2f}МГц')
        self.ui.label_23.setText(f'{s[3]:.2f}МГц')
        self.ui.label_24.setText(f'{s[0]:.2f}МГц')
        self.ui.progressBar.setValue(s[1])
        self.ui.label_25.setText(f'{s[4]}')
        self.ui.label_26.setText(f'{s[5]}')
        self.ui.label_27.setText(f'{s[6]}')
        self.ui.progressBar_3.setValue(s[8])

class RunningProcesses(BaseWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        rp = self.getRP()
        self.set_Text(rp)

    def initializationUi(self):
        self.ui = UI_RunningProcesses()

    def getRP(self):
        return subprocess.check_output('powershell -Executionpolicy ByPass -Command Get-Process').decode(
            encoding='cp866')

    def set_Text(self, rp):
        self.ui.textEdit.setText(rp)


class Services(RunningProcesses):
    def __init__(self, parent=None):
        super().__init__(parent)

    def initializationUi(self):
        self.ui = UI_Service()

    def getRP(self):
        return subprocess.check_output('powershell -Executionpolicy ByPass -Command Get-Service').decode(
            encoding='cp866')


class ManagerTask(RunningProcesses):
    def __init__(self, parent=None):
        super().__init__(parent)

    def initializationUi(self):
        self.ui = UI_ManagerTask()

    def getRP(self):
        return subprocess.check_output('powershell -Executionpolicy ByPass -Command Get-ScheduledTask').decode(
            encoding='cp866')


if __name__ == '__main__':
    main()
