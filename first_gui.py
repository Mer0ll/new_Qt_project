from PySide6 import QtWidgets
from ui_first_gui import Ui_Form


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
