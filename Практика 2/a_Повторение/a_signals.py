"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets
from a1_signals import Ui_MainWindow


def revers_(str_: str) -> str:
    return str_[::-1]


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.initUi()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()


    # def initUi(self):
    #     self.lineEditInput = QtWidgets.QLineEdit()
    #     self.lineEditMirror = QtWidgets.QLineEdit()
    #     self.pushButtonMirror = QtWidgets.QPushButton("pushButton")
    #
    #     layout_1 = QtWidgets.QHBoxLayout()
    #
    #     layout_1.addWidget(self.lineEditInput)
    #     layout_1.addWidget(self.lineEditMirror)
    #     layout_1.addWidget(self.pushButtonMirror)
    #
    #     main_layout = QtWidgets.QVBoxLayout()
    #     main_layout.addLayout(layout_1)
    #     main_layout.addWidget(self.pushButtonMirror)
    #
    #     self.setLayout(main_layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.pushButton.clicked.connect(self.setlineEditMirror)

    def setlineEditMirror(self):
        self.ui.lineEditMirror.setText(revers_(self.ui.lineEditInput))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
