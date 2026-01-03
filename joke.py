import  sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt

class Some_joke(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,200,400,300)
        self.word_input=QLineEdit(self)
        self.word_input.setPlaceholderText("ENTER a word")
        self.search_button=QPushButton("search meaning",self)
        self.result=QLabel("meaning appear",self)
        self.result.setWordWrap(True)
        

        self.initUI()
        self.search_button.clicked.connect(self.get_word)

    def initUI(self):

        self.setWindowTitle("dictonary word")
        self.result.setAlignment(Qt.AlignCenter)
        vbox=QVBoxLayout(self)
        vbox.addWidget(self.word_input)
        vbox.addWidget(self.search_button)
        vbox.addWidget(self.result)
        self.setLayout(vbox)

        self.search_button.setStyleSheet("font-family:Arial;"
                                         "font-size:45px;")
        self.word_input.setStyleSheet("font-family:Arial;"
                                         "font-size:45px;")
        self.result.setStyleSheet("font-family:Arial;"
                                         "font-size:45px;")


    def get_word(self):
        word=self.word_input.text()
        if not word:
            self.result.setText("Enter a word")
        url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
            if response.status_code==200:
                self.display_result(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 404:
                    self.display_error("NOT FOUND\nWORD NOT FOUND")
                case 429:
                    self.display_error("too many requests")
                case _:
                    self.display_error(f"HTTP ERROR\n{http_error}")

    def display_result(self,data):
        if isinstance(data,list):
            meaning=data[0]["meanings"][0]["definitions"][0]["definition"]
            self.result.setText(meaning)
    
    def display_error(self,message):
        self.result.setText(message)
        
def main():
    app=QApplication(sys.argv)
    joke=Some_joke()
    joke.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()