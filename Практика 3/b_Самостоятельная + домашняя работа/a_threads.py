"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil
import requests
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
            self.systemInfoReceived.emit(
                [cpu_value, ram_value])  # с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # с помощью функции .sleep() приостановите выполнение цикла на время self.delay
        self.finished.emit()


class WeatherHandler(QtCore.QThread):
    #  Пропишите сигналы, которые считаете нужными
    weatherhandler = QtCore.Signal(dict)

    def __init__(self, lat=59.94, lon=30.31, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 3600
        self.__status = True

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:
        # настройте метод для корректной работы

        while self.__status:
            # Примерный код ниже
            response = requests.get(self.__api_url)
            data = response.json()
            N = '{:.2f}'.format(float(data['latitude']))
            E = '{:.2f}'.format(float(data['longitude']))
            data_dict = {'Координаты': f"{N} N {E} E",
                         'Температура': f"{data['current_weather']['temperature']}",
                         'Скорость ветра': f"{data['current_weather']['windspeed']} м/с"}

            self.weatherhandler.emit(data_dict)
            time.sleep(self.__delay)
        self.finished1.emit()


class Window(QtWidgets.QWidget):
    def __init__(self, patern=None):
        super().__init__(patern)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initThread()
        self.initSignal()

    def initThread(self):
        self.threadInfo = SystemInfo()  # создаем экземпляр
        self.threadWeatwer = WeatherHandler()  # создаем экземпляр

    def initSignal(self):
        self.ui.pushButton.clicked.connect(self.startProccesSystemInfo)
        self.threadInfo.systemInfoReceived.connect(self.reportProgress)

        self.ui.pushButton_2.clicked.connect(self.startProccesWeatherHandler)
        self.threadWeatwer.weatherhandler.connect(self.reportProgressWeatherHandler)

        self.threadInfo.finished.connect(self.threadInfo.deleteLater)

        self.threadWeatwer.finished.connect(self.threadWeatwer.deleteLater)

    def startProccesSystemInfo(self):
        self.threadInfo.start()  # запуск потока SystemInfo

    def startProccesWeatherHandler(self):
        self.threadWeatwer.start()  # запуск потока WeatherHandler

    def reportProgress(self, s):
        """
         Приём данных из потока и обработка их в основном цикле приложения
        """
        self.ui.lineEdit.setText(f'{s[0]}')
        self.ui.lineEdit_2.setText(f'{s[1]}%')

    def reportProgressWeatherHandler(self, p):
        """
         Приём данных из потока и обработка их в основном цикле приложения
        """
        str_ = ''
        for key in p.keys():
            str_ += f'{key}: {p[key]}\n'
        # print(str_)
        self.ui.plainTextEdit.setPlainText(str_)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
