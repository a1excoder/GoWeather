from PySide2.QtWidgets import *
from gui import Ui_Form
import requests
import sys


url = 'http://api.openweathermap.org/data/2.5/weather'
api = open('sysFiles/config.txt', 'r').readline()


if __name__ == '__main__':
	app = QApplication(sys.argv)


	Form = QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()

def search():

	if ui.lineEdit.text() == '':
		ui.label_2.setText("Введите название города (Поселка)")
	else:

		try:
			params = {'APPID': api, 'q': ui.lineEdit.text(), 'units': 'metric', 'lang': 'ru'}
			result = requests.get(url, params=params)
			weather = result.json()

			if weather["main"]['temp'] < 10:
				state = "Сейчас холодно!"
			elif weather["main"]['temp'] < 20:
				state = "Сейчас прохладно!"
			elif weather["main"]['temp'] > 38:
				state = "Сейчас жарко!"
			else:
				state = "Сейчас отличная температура!"

			ui.label_2.setText("В городе " + str(weather["name"]) + " температура " + str(
				float(weather["main"]['temp'])) + " °C" + "\n" +
							   "Максимальная температура " + str(float(weather['main']['temp_max'])) + " °C" + "\n" +
							   "Минимальная температура " + str(float(weather['main']['temp_min'])) + " °C" + "\n" +
							   "Скорость ветра " + str(float(weather['wind']['speed'])) + "\n" +
							   "Давление " + str(float(weather['main']['pressure'])) + "\n" +
							   "Влажность " + str(float(weather['main']['humidity'])) + "\n" +
							   "Видимость " + str(weather['visibility']) + "\n" +
							   "Описание " + str(weather['weather'][0]["description"]) + "\n" + "\n" + state)

		except KeyError:
			ui.label_2.setText("Город " + ui.lineEdit.text() + " не найден")



ui.pushButton.clicked.connect( search )

sys.exit(app.exec_())
