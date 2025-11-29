from vpython import *
import math

# Imposta la scena
scene.background = color.black
scene.title = "Scena 1 – L’ossigeno si rivela"
scene.width = 1000
scene.height = 700

# Luce direzionale
distant_light(direction=vector(1, 1, 1), color=color.white)

# Molecola di ossigeno inizialmente densa
ossigeno = sphere(pos=vector(0, 0, 0), radius=0.4, color=color.cyan, opacity=1)

# Nucleo tipo morula: gruppo di sfere viola
nucleo = []
for i in range(12):  # 6 protoni + 6 neutroni
    angolo = i * math.pi / 6
    r = 0.1
    x = r * math.cos(angolo)
    y = r * math.sin(angolo)
    z = 0.05 * math.sin(i)
    particella = sphere(pos=ossigeno.pos + vector(x, y, z), radius=0.05, color=color.purple, opacity=0.8)
    nucleo.append(particella)

# Sei elettroni gialli brillanti
elettroni = []
for i in range(6):
    angolo = i * math.pi / 3
    raggio = 0.25
    pos = ossigeno.pos + vector(raggio * math.cos(angolo), raggio * math.sin(angolo), 0)
    e = sphere(pos=pos, radius=0.03, color=color.yellow, emissive=True)
    elettroni.append(e)

# Funzione per far orbitare gli elettroni
def orbita(elettrone, centro, raggio, velocità, angolo_base):
    angolo = angolo_base + velocità * t
    elettrone.pos = centro + vector(raggio * math.cos(angolo), raggio * math.sin(angolo), 0)

# Animazione per 10 secondi
t = 0
while t < 10:
    rate(60)
    t += 0.05

    # Rotazione dell’ossigeno
    ossigeno.rotate(angle=0.01, axis=vector(0, 1, 0), origin=vector(0, 0, 0))

    # Transizione verso trasparenza
    ossigeno.opacity = max(0.3, 1 - t / 10)

    # Orbite degli elettroni
    for i in range(6):
        orbita(elettroni[i], ossigeno.pos, 0.25, 1.5, i * math.pi / 3)