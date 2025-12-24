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
                    self.display_error("bad request\nplease check your input")
                case 401:
                    self.display_error("unauthorized\nInvalid API key")
                case 403:
                    self.display_error("Forbidden\nAccess is denied")
                case 404:
                    self.display_error("not found\ncity not found")
                case 500:
                    self.display_error("internal server error\nplease try again later")
                case 502:
                    self.display_error("Bad gatway\nInvalide response")
                case 503:
                    self.display_error("service unavailable\nserver is down")
                case 504:
                    self.display_error("Gatway timeout\nno response")

                case _:
                    self.display_error(f"HTTP ERROR\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\n Check internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request time out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects\nchect the url")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Erroe:\n{req_error}")

    def display_error(self,message):
        self.temperature.setStyleSheet("font-size:3opx;")
        self.temperature.setText(message)
        self.sun_Emoji.clear()
        self.description.clear()

    def display_weather(self,data):
        self.temperature.setStyleSheet("font-size:75px;")
        temp_k=data["main"]["temp"]
        temp_c=temp_k-273.15
        temp_f=(temp_k * 9/5) - 459.67
        weather_description= data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        
        self.temperature.setText(f"{temp_f:.0f}\u2109")
        self.sun_Emoji.setText(self.get_weather_emoji(weather_id))
        self.description.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200<= weather_id <= 232:
            return"\U0001F329"
        elif 300 <= weather_id <= 321:
            return"\U0001F326"
        elif 500 <= weather_id <= 531:
            return"\U0001F327"
        elif 600 <= weather_id <= 622:
            return"\u2744"
        elif 701 <= weather_id <=741:
            return"\U0001F32B"
        elif weather_id==762:
            return"🌋"
        elif weather_id==771:
            return"💨"
        elif weather_id==781:
            return"\U0001F329"
        elif weather_id==800:
            return"\u2600"
        elif 801 <= weather_id <= 804:
            return"\u2601"
        else:
            return""

def main():
    app=QApplication(sys.argv)
    wether=WatherApp()
    wether.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()