import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np

x = np.random.random(1000)*200-100
y = np.random.random(1000)*200-100
color = np.random.random(1000)


plt.scatter(x,y, c=np.random.rand(len(x),3)) # "b" für Blau, g - grün, k - schwarz / "o" für punkte, "x" kreuz / "-" für verbinden, "--" gestrichelt, ":" punkelte linie
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal") #x- und y-Achse gelich gross
plt.show()