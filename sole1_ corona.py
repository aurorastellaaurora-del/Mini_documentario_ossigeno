from vpython import *
import math
import time

# -------------------------
# Impostazioni generali
# -------------------------
scene.background = color.black
scene.width = 1000
scene.height = 700
scene.title = "Sole in apertura"
distant_light(direction=vector(1,1,1), color=color.white)

# Posizione camera iniziale
scene.camera.pos = vector(0,0,15)
scene.camera.axis = vector(0,0,-15)

# -------------------------
# Sole
# -------------------------
sole = sphere(pos=vector(0,0,0), radius=2, color=vector(1,0.8,0), emissive=True)

# -------------------------
# Pulviscolo / flare
# -------------------------
n_pulviscolo = 200
pulviscolo = []
for _ in range(n_pulviscolo):
    theta = 2*math.pi*random()
    phi = math.acos(2*random() - 1)
    r = 2 + 0.5*random()
    x = r*math.sin(phi)*math.cos(theta)
    y = r*math.sin(phi)*math.sin(theta)
    z = r*math.cos(phi)
    p = sphere(pos=vector(x,y,z), radius=0.03, color=color.orange, opacity=0.6)
    pulviscolo.append(p)

# -------------------------
# Animazione apertura
# -------------------------
t0 = time.time()
while time.time() - t0 < 10:  # 10 secondi
    rate(60)
    t = time.time() - t0

    # Piccolo pulsare del Sole
    sole.radius = 2 + 0.2*math.sin(2*math.pi*t/2)

    # Leggera rotazione dei pulviscoli
    for p in pulviscolo:
        p.rotate(angle=0.005, axis=vector(0,1,0), origin=vector(0,0,0))
