"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль и в plainTextEdit,
размещённый на виджете, при выводе события указывать время, когда оно произошло
"""

from PySide6 import QtWidgets, QtCore
from time import ctime
from b1_events import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def event(self, event: QtCore.QEvent) -> bool:
        """
        Перехват всех событий

        :param event: QtCore.QEvent
        :return: bool
        """

        output_string = f'time: {ctime()}, event = {str(event)}'
        self.ui.plainTextEdit.insertPlainText(output_string + "\n")
        print(output_string)
        return super().event(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
