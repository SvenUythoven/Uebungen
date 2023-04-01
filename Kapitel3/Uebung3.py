import math

class Figur:
    def __init__(self):
        self.name = "Figur"

    def Umfang(self):
        return 0

    def __str__(self):
        return self.name
    
class Punkt(Figur):
    def __init__(self, x ,y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt ({self.x},{self.y})"
    
class Kreis(Figur):   ## Kreis(verbindung)
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")  
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def umfang(self):
        return 2 * math.pi * self.radius
    
class Dreieck(Figur):
    def __init__(self, punkta, punktb, punktc):
        super().__init__("Dreieck")
        self.punkta = punkta
        self.punktb = punktb
        self.punktc = punktc

    def umfang(self):
        return 
