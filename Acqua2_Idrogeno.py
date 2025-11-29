# © Aurora Stella - MIT License


from vpython import *
import math

# Imposta la scena
scene.background = color.black
scene.title = "Scena 2 – Gli idrogeni si preparano"
scene.width = 1000
scene.height = 700

# Luce direzionale
distant_light(direction=vector(1, 1, 1), color=color.white)

# Posizioni iniziali
pos1 = vector(-1, 0.5, 0)
pos2 = vector(1, -0.5, 0)

# Atomi di idrogeno (trasparenti, uguali)
idrogeno1 = sphere(pos=pos1, radius=0.2, color=color.red, opacity=0.5)
idrogeno2 = sphere(pos=pos2, radius=0.2, color=color.red, opacity=0.5)

# Protoni centrali
protone1 = sphere(pos=pos1, radius=0.07, color=color.red, opacity=0.8)
protone2 = sphere(pos=pos2, radius=0.07, color=color.red, opacity=0.8)

# Elettroni gialli brillanti
elettrone1 = sphere(pos=pos1 + vector(0.25, 0, 0), radius=0.03, color=color.yellow, emissive=True)
elettrone2 = sphere(pos=pos2 + vector(0.25, 0, 0), radius=0.03, color=color.yellow, emissive=True)

# Funzione per orbite attorno al proprio nucleo
def orbita(elettrone, centro, raggio, velocità, angolo_base):
    angolo = angolo_base + velocità * t
    elettrone.pos = centro + vector(raggio * math.cos(angolo), raggio * math.sin(angolo), 0)

# Animazione per 10 secondi
t = 0
while t < 10:
    rate(60)
    t += 0.05

    # Rotazione degli atomi
    idrogeno1.rotate(angle=0.01, axis=vector(0, 1, 0), origin=pos1)
    idrogeno2.rotate(angle=0.01, axis=vector(0, 1, 0), origin=pos2)

    # Orbite corrette
    orbita(elettrone1, pos1, 0.25, 2, 0)
    orbita(elettrone2, pos2, 0.25, -2, 0)