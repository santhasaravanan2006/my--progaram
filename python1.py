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
        self.temperature=QLabel(self)
        self.sun_Emoji=QLabel(self)
        self.description=QLabel(self)
        self.initUI()

        self.get_Weather.clicked.connect(self.get_weather)

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
        
        }
        """)
        
        self.description.setStyleSheet("font-size:50px;")

    def get_weather(self):
        api_key="e909a4ece58e87a97adca464ad516baf"
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
            if data["cod"]==200:
               self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    print("bad request\nplease check your input")
                case 401:
                    print("unauthorized\nInvalid API key")
                case 403:
                    print("Forbidden\nAccess is denied")
                case 404:
                    print("not found\ncity not found")
                case 500:
                    print("internal server error\nplease try again later")
                case 502:
                    print("Bad gatway\nInvalide response")
                case 503:
                    print("service unavailable\nserver is down")
                case 504:
                    print("Gatway timeout\nno response")

                case _:
                    print(f"HTTP ERROR\n{http_error}")
                
                
                    

            pass
        except requests.exceptions.RequestException:
            pass
            

    def display_error(self,message):
        pass
    def display_weather(self,data):
        print(data)



def main():
    app=QApplication(sys.argv)
    wether=WatherApp()
    wether.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()