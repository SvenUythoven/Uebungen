import math

class Figur:
    def __init__(self, name):
        self.name = name

    def Umfang(self):
        return 0

    def __str__(self):
        return self.name
    
    def dist(self):
        return 0
    
class Punkt(Figur):
    def __init__(self, x ,y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt ({self.x},{self.y})"
    
    def dist(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

    
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
        return (self.punkta.dist(self.punktb))+(self.punktb.dist(self.punktc))+(self.punktc.dist(self.punkta))
class Rechteck(Figur):
    def __init__(self, punkta, punktb, punktc, punktd):
        super().__init__("Rechteck")
        self.punkta = punkta
        self.punktb = punktb
        self.punktc = punktc
        self.punktd = punktd

class Polygon(Figur):
    def __init__(self,matrix):
        super().__init__("Polygon")
        self.matrix = matrix
    
    
    def umfang(self):
        return self.punkta.dist(self.punktb)+self.punktb.dist(self.punktc)+self.punktc.dist(self.punktd)+self.punktd.dist(self.punkta)

p1 = Punkt(0,0)
p2 = Punkt(4,0)
p4 = Punkt(4,4)
p3 = Punkt(0,4)

d1 = Dreieck(p1,p2,p3)
r1 = Rechteck(p1,p2,p3,p4)

print(d1.umfang())
print(r1)



         
