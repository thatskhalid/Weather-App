import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, 
    QPushButton, QVBoxLayout)



from PyQt5.QtCore import Qt  # used for alignment

class WeatherApp(QWidget):  # will inherit from "QWidget"
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # arguments
    weather_app = WeatherApp()
    weather_app.show()    
    sys.exit(app.exec_())
