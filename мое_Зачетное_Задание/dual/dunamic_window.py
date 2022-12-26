from PySide6 import QtWidgets
import sys


def main():
    app = QtWidgets.QApplication()
    window = DWindow()
    window.show()
    app.exec()


class DWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        txt = sys.argv
        self.initUI(txt[1])

    def initUI(self, txt):
        main_layout = QtWidgets.QVBoxLayout()

        btn = QtWidgets.QPushButton(txt)
        lbl = QtWidgets.QLabel(txt)

        main_layout.addWidget(btn)
        main_layout.addWidget(lbl)

        self.setLayout(main_layout)


if __name__ == '__main__':
    main()
