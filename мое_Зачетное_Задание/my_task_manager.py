from PySide6 import QtWidgets, QtCore
from ui_my_task_manager import Ui_Form


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

        dialog_boxes = ['',
                        'Процессор, количество ядер, текущая загрузка',
                        'Оперативная памяти, загрузка',
                        'Информация о жестких дисках']

        self.ui.comboBox.addItems(dialog_boxes)


if __name__ == '__main__':
    main()
