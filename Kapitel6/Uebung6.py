from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import *
from PyQt5.uic import *
import urllib.parse


class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel6/showmap.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        self.breit = self.lineEdit.text()
        self.laenge = self.lineEdit_2.text()
        query = 'Hellö Wörld@'
        a = urllib.parse.quote(query)  
        path = f"https://www.google.ch/maps/place/{self.breit},{self.laenge}"
        QDesktopServices.openUrl(QUrl(path))
        

app = QApplication([])
win = UIFenster()
app.exec()