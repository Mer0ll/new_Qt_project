from PySide6 import QtWidgets, QtCore, QtGui
from ui_my_task_manager_mainWindow import Ui_mainForm
from ui_my_task_manager_cildWindowServices import Ui_Form as UI_Service
from ui_my_task_manager_cildManagerTask import Ui_Form as UI_ManagerTask
from ui_my_task_manager_cildRunningProcesses import Ui_Form as UI_RunningProcesses
import psutil
import platform
import subprocess
import time


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
        # self.initCildWindow()

    def setAboutSystem(self):
        uname = platform.uname()
        self.ui.label_6.setText(uname.system)
        self.ui.label_7.setText(uname.node)
        self.ui.label_8.setText(uname.release)
        self.ui.label_9.setText(uname.version)
        self.ui.label_10.setText(uname.machine)

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


class ResourceMonitor(QtWidgets.QWidget):
    ...


class RunningProcesses(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initializationUi()
        self.ui.setupUi(self)
        self.initSignals()
        rp = self.getRP()
        self.set_Text(rp)

    def initializationUi(self):
        self.ui = UI_RunningProcesses()

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()

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
