from PySide6 import QtWidgets

from ui_first_gui import Ui_Form


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initsignal()

    @staticmethod
    def flip_the_line(str_: str) -> str:
        return str_[::-1]

    def initsignal(self):
        self.ui.button.clicked.connect(self.answer)

    def answer(self):
        self.ui.output_2.setText(self.flip_the_line(self.ui.input_1.text()))


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()

