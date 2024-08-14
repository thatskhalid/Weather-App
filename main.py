import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, 
    QPushButton, QVBoxLayout)



from PyQt5.QtCore import Qt  # used for alignment

class WeatherApp(QWidget):  # this class weatherapp will inherit from "QWidget"
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70°F", self)
        self.emoji_label = QLabel("⛅", self)
        self.description_label = QLabel("Sunny", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

if __name__ == "__main__":
    app = QApplication(sys.argv)  # arguments
    weather_app = WeatherApp()
    weather_app.show()    
    sys.exit(app.exec_()) #handle events within the application, like closing the window
    
