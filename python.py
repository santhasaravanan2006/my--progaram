import sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt

class WatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.city_label=QLabel("Enter city name",self)
        self.city_input=QLineEdit(self)
        self.get_Weather=QPushButton("GET WEATHER",self)
        self.temperature=QLabel("70'F",self)
        self.sun_Emoji=QLabel("\U0001F31E",self)
        self.description=QLabel("sunny",self)
        self.initUI()

    def initUI(self):

        self.setWindowTitle("wether app")
        

        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)
        self.sun_Emoji.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)


        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_Weather.setObjectName("get_Weather")
        self.temperature.setObjectName("temperature")
        self.sun_Emoji.setObjectName("sun_Emoji")
        self.description.setObjectName("descripition")

        vbox=QVBoxLayout(self)

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_Weather)
        vbox.addWidget(self.temperature)
        vbox.addWidget(self.sun_Emoji)
        vbox.addWidget(self.description)
        self.setLayout(vbox)

        self.setStyleSheet("""
        QLabel, QPushButton{
        font-family:calibri;
        }
        QLabel#city_label
        {
        font-size:40px;
        font-style:italic;
        }
        QLineEdit#city_input{
        font-size:40px;
        }
        QPushButton#get_Weather{
        font-size:40px;
        font-weight:bold;
        }
        QLabel#temperature{
        font-size:75px;
        }
        QLabel#sun_Emoji{
        font-size:100px;
        }
        QLabel#description{
        font-size:50px;
        }
        """)
        
        self.description.setStyleSheet("font-size:50px;")





def main():
    app=QApplication(sys.argv)
    wether=WatherApp()
    wether.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()