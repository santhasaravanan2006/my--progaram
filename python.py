import sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt

class WatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.city_lable=QLabel("Enter city name",self)
        self.city_input=QLineEdit(self)
        self.get_Weather=QPushButton("GET WEATHER",self)
        self.temperature=QLabel("70'F",self)
        self.sun_Emoji=QLabel("\U0001F31E",self)
        self.description=QLabel("sunny",self)
        



def main():
    app=QApplication(sys.argv)
    wether=WatherApp()
    wether.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()