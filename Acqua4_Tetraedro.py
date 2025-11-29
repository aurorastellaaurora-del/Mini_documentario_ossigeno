
from vpython import *
import math
import time

# Imposta la scena
scene.background = color.black
scene.title = "Scena 4 – Il Tetraedro dell’Acqua"
scene.width = 1000
scene.height = 700

# Luce direzionale
distant_light(direction=vector(1, 1, 1), color=color.white)

# Molecola d'acqua al centro
ossigeno = sphere(pos=vector(0, 0, 0), radius=0.4, color=color.cyan, opacity=1)
idrogeno1 = sphere(pos=vector(0.6, 0.4, 0), radius=0.2, color=color.red, opacity=1)
idrogeno2 = sphere(pos=vector(0.6, -0.4, 0), radius=0.2, color=color.red, opacity=1)
legame1 = cylinder(pos=ossigeno.pos, axis=idrogeno1.pos - ossigeno.pos, radius=0.02, color=color.orange, opacity=0.8)
legame2 = cylinder(pos=ossigeno.pos, axis=idrogeno2.pos - ossigeno.pos, radius=0.02, color=color.orange, opacity=0.8)

# Vertici del tetraedro
v1 = vector(0, 1, 0.7)
v2 = vector(-1, -0.8, 0.7)
v3 = vector(1, -0.8, 0.7)
v4 = vector(0, 0, -1.2)

# Salva i vertici in una lista
vertici = [v1, v2, v3, v4]
linee = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]

# Crea le curve iniziali
curve_objs = []
for i,j in linee:
    c = curve(pos=[vertici[i], vertici[j]], radius=0.01, color=color.white)
    curve_objs.append(c)

# Timer reale per 10 secondi
start_time = time.time()
while time.time() - start_time < 10:
    rate(60)
    angolo = 0.01
    asse = vector(0, 1, 0)

    # Ruota i vertici
    for i in range(len(vertici)):
        vertici[i] = vertici[i].rotate(angle=angolo, axis=asse)

    # Ricrea le curve aggiornate
    for k in range(len(linee)):
        i, j = linee[k]
        curve_objs[k].clear()
        curve_objs[k].append(pos=vertici[i])
        curve_objs[k].append(pos=vertici[j])

    # Ruota la molecola
    ossigeno.rotate(angle=angolo, axis=asse, origin=vector(0, 0, 0))
    idrogeno1.rotate(angle=angolo, axis=asse, origin=vector(0, 0, 0))
    idrogeno2.rotate(angle=angolo, axis=asse, origin=vector(0, 0, 0))
    legame1.axis = idrogeno1.pos - ossigeno.pos
    legame2.axis = idrogeno2.pos - ossigeno.pos