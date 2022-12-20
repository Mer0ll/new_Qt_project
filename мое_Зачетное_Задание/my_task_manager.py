from PySide6 import QtWidgets, QtCore, QtGui
from ui_my_task_manager_mainWindow import Ui_mainForm
import psutil
import platform
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
        self.initCildWindow()

    def setAboutSystem(self):
        uname = platform.uname()
        self.ui.label_6.setText(uname.system)
        self.ui.label_7.setText(uname.node)
        self.ui.label_8.setText(uname.release)
        self.ui.label_9.setText(uname.version)
        self.ui.label_10.setText(uname.machine)

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.openChildWindow)

    def initCildWindow(self):
        self.cildWindowResourceMonitor = ResourceMonitor()
        self.cildWindowRunningProcesses = RunningProcesses()
        self.cildWindowServices = Services()
        self.cildWindowManagerTask = ManagerTask()

    def openChildWindow(self):
        if self.ui.comboBox.currentText() == 'Монитор ресурсов':
            self.cildWindowResourceMonitor.show()
        elif self.ui.comboBox.currentText() == 'Запущенные процессы':
            self.cildWindowRunningProcesses.show()
        elif self.ui.comboBox.currentText() == 'Службы':
            self.cildWindowServices.show()
        elif self.ui.comboBox.currentText() == 'Планировщик задач':
            self.cildWindowManagerTask.show()


class ResourceMonitor(QtWidgets.QWidget):
    ...


class RunningProcesses(QtWidgets.QWidget):
    ...


class Services(QtWidgets.QWidget):
    ...


class ManagerTask(QtWidgets.QWidget):
    ...


if __name__ == '__main__':
    main()
