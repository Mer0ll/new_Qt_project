from PySide6 import QtWidgets, QtCore, QtGui
import psutil
import time
import platform
from ui_my_task_manager_cildResourceMonitor import Ui_Form as UI_rm


def main():
    app = QtWidgets.QApplication()

    taskmanager = ResourceMonitor()
    taskmanager.show()

    app.exec()


class WorkerRM(QtCore.QThread):
    workerCPU = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        cpufreg = psutil.cpu_freq()
        while True:
            currentfreq = cpufreg.current  # Текущая частота
            totalCPUusage = psutil.cpu_percent()  # Общая загруженность процессора
            self.workerCPU.emit([currentfreq,
                                 totalCPUusage])
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
        self.ui.label_2.setText(uname.processor)
        self.ui.lineEdit_2.setText(f'{psutil.cpu_count(logical=True)}')
        self.ui.lineEdit_3.setText(f'{psutil.cpu_count(logical=False)}')

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
        self.ui.lineEdit.setText(f'{s[0]:.2f}')
        self.ui.progressBar.setValue(s[1])


if __name__ == '__main__':
    main()
