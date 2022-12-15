"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets

from ui.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.ui.comboBox.addItems(['oct', 'hex', 'bin', 'dec'])

    def initSignals(self):
        self.ui.dial.valueChanged.connect(self.setDataLSD1)
        self.ui.horizontalSlider.valueChanged.connect(self.setDataLSD2)

        # self.ui.comboBox.valueChanged.connect(self.setLCDmod)
        self.ui.comboBox.currentTextChanged.connect(self.setLCDmod)

    def setDataLSD1(self):
        self.ui.lcdNumber.display(self.ui.dial.value())
        self.ui.horizontalSlider.setValue(self.ui.dial.value())

    def setDataLSD2(self):
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())
        self.ui.dial.setValue(self.ui.horizontalSlider.value())

    def setLCDmod(self):
        if self.ui.comboBox.currentText() == 'hex':
            self.ui.lcdNumber.setHexMode()
        if self.ui.comboBox.currentText() == 'dec':
            self.ui.lcdNumber.setDecMode()
        if self.ui.comboBox.currentText() == 'oct':
            self.ui.lcdNumber.setOctMode()
        if self.ui.comboBox.currentText() == 'bin':
            self.ui.lcdNumber.setBinMode()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
