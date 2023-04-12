import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import urllib.parse
query = 'Hellö Wörld@'
a = urllib.parse.quote(query)  


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI - Programierung")

        #layout erzeugen
        #layout = ... # QVBoxLayout(), QHBoxLayout(), QGridlayout(), QFormLayout()...
        layout = QFormLayout()

        #gui Elemente erstellen------------------------------------------------
        self.Vorname = QLineEdit()
        self.Name = QLineEdit()
        self.Geburtstag = QDateEdit()
        self.Adresse = QLineEdit()
        self.Postleizahl = QLineEdit()
        self.Ort = QLineEdit()
        self.Land = QComboBox()
        self.kartezeigen = QPushButton("Auf Karte zeigen")
        self.Laden = QPushButton("Laden")
        self.Button = QPushButton("Save")
        

        self.Land.addItems(["Schweiz", "Deutschland", "Österreich"])
    

        #gui Elemente dem Layout hinzufügen------------------------------------
        layout.addRow("Vorname:", self.Vorname)
        layout.addRow("Name:", self.Name)
        layout.addRow("Geburtstag:", self.Geburtstag)
        layout.addRow("Adresse:", self.Adresse)
        layout.addRow("Postleizahl:", self.Postleizahl)
        layout.addRow("Ort:", self.Ort)
        layout.addRow("Land:", self.Land)
        layout.addRow(self.kartezeigen)
        layout.addRow(self.Laden)
        layout.addRow(self.Button)
        

        #Menubar:--------------------------------------------------------------
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        view = menubar.addMenu("View")


        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)
        self.karte = QAction("Karte", self)

        file.addAction(self.save)
        file.addAction(self.quit)
        view.addAction(self.karte)

        # Button Connection----------------------------------------------------     
        self.Button.clicked.connect(self.textFile)
        self.save.triggered.connect(self.textFile)
        self.kartezeigen.clicked.connect(self.zeigen)
        self.karte.triggered.connect(self.zeigen)
        self.quit.triggered.connect(self.close)
        self.Laden.clicked.connect(self.openFile)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    #openFile------------------------------------------------------------------
    def openFile(self):
        filename, filter = QFileDialog.getOpenFileName(self, "Datei öfnen", "", "Text Files (*.txt)")
        file = open(filename, "r", encoding = "utf-8")
        data = file.read()
        list = data.split(",")
        
        self.Vorname.setText(list[0])
        self.Name.setText(list[1])
        self.Geburtstag.setDate(QDate.fromString(list[2], "dd.MM.yyyy"))
        self.Adresse.setText(list[3])
        self.Postleizahl.setText(list[4])
        self.Ort.setText(list[5])
        self.Land.setCurrentText(list[6])


        file.close()


    # Karte anzeigen:----------------------------------------------------------------    
    def zeigen(self):
        a = self.Adresse.text()
        o = self.Ort.text()
        l = self.Land.currentText()

        path = f"https://www.google.ch/maps/place/{a}+{o}+{l}"

        QDesktopServices.openUrl(QUrl(path))

    # Text File:----------------------------------------------------------------    
    def textFile(self):
        
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichen", "","Text Datei (*.txt)")
        
        v = self.Vorname.text()
        n = self.Name.text()
        g = self.Geburtstag.date().toString("dd.MM.yyyy") # .date().toString("dd.MM.yyyy") um das format zu definieren
        a = self.Adresse.text()
        p = self.Postleizahl.text()
        o = self.Ort.text()
        l = self.Land.currentText()
        text = f"{v},{n},{g},{a},{p},{o},{l}"
        file = open(filename, "w",encoding = "utf-8")  

        file.write(text)

        file.close()
        print("Die Daten wurden mit erfolg gespeichert")

    def close(self):
        self.close()

    #--------------------------------------------------------------------------

    

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()



