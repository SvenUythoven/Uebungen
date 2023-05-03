from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)

        text1 = QLabel("Koefizienten:")
        self.koef = QLineEdit("[]")
        text2 = QLabel("Anzahl Punkte:")
        self.punkte = QLineEdit()
        text3 = QLabel("Farbe:")
        self.color = QComboBox()
        button = QPushButton("Plot")

        self.color.addItems(["b", "k", "g", "r"])

        layout.addWidget(self.canvas)
        layout.addWidget(text1)
        layout.addWidget(self.koef)
        layout.addWidget(text2)
        layout.addWidget(self.punkte)
        layout.addWidget(text3)
        layout.addWidget(self.color)
        layout.addWidget(button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        button.clicked.connect(self.plot)

    def plot(self):
        plt.clf() #clear figure
        try:
            f = np.poly1d(eval(self.koef.text()))
            x = np.linspace(0,10,eval(self.punkte.text()))
            y = f(x)
            color = self.color.currentText()
        except:
            QMessageBox.critical(self, "Fehler" , "Bitte Eingabe überprüfen")     
        try:
            plt.plot(x, y, f"{color}o-")
            plt.axis("equal")
            self.canvas.draw()
        except:
            QMessageBox.critical(self, "Fehler" , "Bitte Eingabe überprüfen")




app = QApplication([])
window = Window()
app.exec()

