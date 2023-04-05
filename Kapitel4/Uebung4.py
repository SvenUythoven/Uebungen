import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

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
        layout.addRow(self.Button)

        #Menubar:--------------------------------------------------------------
        menubar = self.menuBar()
        file = menubar.addMenu("File")

        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)

        file.addAction(self.save)
        file.addAction(self.quit)

        # Button Connection----------------------------------------------------     
        self.Button.clicked.connect(self.textFile)
        self.save.triggered.connect(self.textFile)
        self.quit.triggered.connect(self.close)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    # Text File:----------------------------------------------------------------    
    def textFile(self):
        text = f"{self.Vorname.text()},{self.Name.text()},{self.Geburtstag.text()},{self.Adresse.text()},{self.Postleizahl.text()},{self.Ort.text()},{self.Land.currentText()}"
        file = open("output.txt.", "w",encoding = "utf-8")  

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



