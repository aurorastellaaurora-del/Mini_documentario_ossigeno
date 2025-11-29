from vpython import *
import math
import time
from random import random, uniform, choice

# -------------------------
# Impostazioni generali
# -------------------------
scene.background = color.black
scene.width = 1000
scene.height = 700
scene.title = "Sole dinamico"
distant_light(direction=vector(1,1,1), color=color.white)

scene.camera.pos = vector(0,0,20)
scene.camera.axis = vector(0,0,-20)

# -------------------------
# Sole
# -------------------------
sole = sphere(pos=vector(0,0,0), radius=2, color=vector(1,0.8,0), emissive=True)

# -------------------------
# Macchie solari
# -------------------------
n_macchie = 15
macchie = []
for _ in range(n_macchie):
    theta = 2*math.pi*random()
    phi = math.acos(2*random() - 1)
    r = 1.8
    x = r*math.sin(phi)*math.cos(theta)
    y = r*math.sin(phi)*math.sin(theta)
    z = r*math.cos(phi)
    m = sphere(pos=vector(x,y,z), radius=0.15*random(), color=vector(0.3,0,0), emissive=True)
    macchie.append(m)

# -------------------------
# Pulviscolo e vortici
# -------------------------
n_pulviscolo = 300
pulviscolo = []
for _ in range(n_pulviscolo):
    theta = 2*math.pi*random()
    phi = math.acos(2*random() - 1)
    r = 2 + 0.3*random()
    x = r*math.sin(phi)*math.cos(theta)
    y = r*math.sin(phi)*math.sin(theta)
    z = r*math.cos(phi)
    c = vector(uniform(0.9,1), uniform(0.5,0.9), 0)  # arancio-giallo
    p = sphere(pos=vector(x,y,z), radius=0.03, color=c, opacity=0.6, emissive=True)
    pulviscolo.append({'obj': p, 'vel': vector(random()-0.5, random()-0.5, random()-0.5)*0.05})

# -------------------------
# Particelle espulse (fiammate)
# -------------------------
n_fiamme = 50
fiamme = []
for _ in range(n_fiamme):
    dir_vec = vector(random()-0.5, random()-0.5, random()-0.5).norm()
    p = sphere(pos=sole.pos, radius=0.05, color=vector(1,0.6,0), emissive=True, opacity=0.8)
    fiamme.append({'obj': p, 'vel': dir_vec*0.1})

# -------------------------
# Animazione 10 secondi
# -------------------------
t0 = time.time()
while time.time() - t0 < 10:
    rate(60)
    t = time.time() - t0

    # Pulsazione e vortici del Sole
    sole.radius = 2 + 0.2*math.sin(2*math.pi*t/3)

    # Ruota i pulviscoli attorno al Sole e cambia colore
    for p in pulviscolo:
        p['obj'].rotate(angle=0.004, axis=vector(0,1,0), origin=sole.pos)
        p['obj'].color = vector(1, 0.5 + 0.4*math.sin(5*t + random()), 0)
        p['obj'].pos += p['vel']  # movimento leggero radiale
        # ritorno se troppo lontano
        if mag(p['obj'].pos) > 4:
            p['obj'].pos = sole.pos + (p['obj'].pos - sole.pos).norm()*2.5

    # Rotazione macchie
    for m in macchie:
        m.rotate(angle=0.002, axis=vector(0,1,0), origin=sole.pos)

    # Muovi le fiammate nello spazio
    for f in fiamme:
        f['obj'].pos += f['vel']
        # scomparsa graduale
        f['obj'].opacity -= 0.005
        if f['obj'].opacity <= 0:
            f['obj'].pos = sole.pos
            f['obj'].opacity = 0.8
            f['vel'] = vector(random()-0.5, random()-0.5, random()-0.5).norm()*0.1
