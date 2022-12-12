"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil
from PySide6 import QtCore, QtWidgets

from ui_b_add_signals import Ui_Form


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(
        list)  # Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  # создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  # переопределить метод run
        if self.delay is None:  # Если задержка не передана в поток перед его запуском
            self.delay = 1  # то устанавливайте значение 1

        while True:  # Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemInfoReceived.emit([cpu_value, ram_value])  # с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # с помощью функции .sleep() приостановите выполнение цикла на время self.delay


class WeatherHandler(QtCore.QThread):
    # TODO Пропишите сигналы, которые считаете нужными

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:
        # TODO настройте метод для корректной работы

        while self.__status:
            # TODO Примерный код ниже
            """
            response = requests.get(self.__api_url)
            data = response.json()
            ваш_сигнал.emit(data)
            sleep(delay)
            """


class Window(QtWidgets.QWidget):
    def __init__(self, patern=None):
        super().__init__(patern)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initTread()
        self.initSignal()

    def initTread(self):
        self.tread_info = SystemInfo()
        # self.tread_weatwer = WeatherHandler()


    def initSignal(self):
        self.ui.pushButton.clicked.connect(self.startProccesSystemInfo)


    def startProccesSystemInfo(self):
        self.tread_info.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
