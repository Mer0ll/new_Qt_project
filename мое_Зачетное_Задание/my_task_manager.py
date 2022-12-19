from PySide6 import QtWidgets, QtCore
from ui_my_task_manager import Ui_Form
import psutil


def main():
    app = QtWidgets.QApplication()

    taskmanager = TaskManager()
    taskmanager.show()

    app.exec()


class TaskManager(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.partitions = psutil.disk_partitions()

    @staticmethod
    def get_size(bytes, suffix='B'):
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < factor:
                return f'{bytes:.2f}{unit}{suffix}'
            bytes /= factor

    def initSignals(self):

        self.ui.pushButton_1.clicked.connect(self.show_dialog_window)

    def show_dialog_window(self):
        selected_dialog_window = self.ui.comboBox.currentText()

        if selected_dialog_window == 'Информация о жестких дисках':
            self.ui.textEdit_4.setPlainText(self.getdiscinfo())

    def getdiscinfo(self):
        result = ''
        for partition in self.partitions:
            result += f'=== Диск: {partition.device}\n'
            result += f' Тип файловой системы: {partition.fstype}\n'
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            result += f'    Общий объем: {self.get_size(partition_usage.total)}\n'
            result += f'    Используется: {self.get_size(partition_usage.used)}\n'
            result += f'    Свободно: {self.get_size(partition_usage.free)}\n'
            # result += f'    Процент: {self.partition_usage.percent} %\n'
        return result


if __name__ == '__main__':
    main()


 # dialog_boxes = ['',
 #                        'Процессор, количество ядер, текущая загрузка',
 #                        'Оперативная памяти, загрузка',
 #                        'Информация о жестких дисках']
 #
 #        self.comboBox.addItems(dialog_boxes)