from vpython import *
import math

# Imposta la scena
scene.background = color.black
scene.title = "Scena 3 – L’incontro e la nascita della molecola"
scene.width = 1000
scene.height = 700

# Luce direzionale
distant_light(direction=vector(1, 1, 1), color=color.white)

# Ossigeno al centro, opaco
ossigeno = sphere(pos=vector(0, 0, 0), radius=0.4, color=color.cyan, opacity=1)

# Due idrogeni in posizione iniziale
idrogeno1 = sphere(pos=vector(-2, 0.5, 0), radius=0.2, color=color.red, opacity=1)
idrogeno2 = sphere(pos=vector(2, -0.5, 0), radius=0.2, color=color.red, opacity=1)

# Legami covalenti iniziali (quasi invisibili)
legame1 = cylinder(pos=ossigeno.pos, axis=idrogeno1.pos - ossigeno.pos, radius=0.005, color=color.orange, opacity=0.05)
legame2 = cylinder(pos=ossigeno.pos, axis=idrogeno2.pos - ossigeno.pos, radius=0.005, color=color.orange, opacity=0.05)

# Lampo finale (inizialmente invisibile)
lampo = sphere(pos=ossigeno.pos, radius=0.01, color=color.white, emissive=True, visible=False)

# Animazione per 10 secondi
t = 0
while t < 10:
    rate(60)
    t += 0.05

    # Avvicinamento graduale degli idrogeni
    if mag(idrogeno1.pos - ossigeno.pos) > 0.6:
        idrogeno1.pos += vector(0.02, -0.005, 0)
        idrogeno2.pos += vector(-0.02, 0.005, 0)

    # Aggiorna i legami covalenti
    legame1.axis = idrogeno1.pos - ossigeno.pos
    legame2.axis = idrogeno2.pos - ossigeno.pos

    # Intensifica il legame covalente (senza diventare un palo!)
    legame1.opacity = min(1, legame1.opacity + 0.01)
    legame2.opacity = min(1, legame2.opacity + 0.01)
    legame1.radius = min(0.02, legame1.radius + 0.0005)
    legame2.radius = min(0.02, legame2.radius + 0.0005)

    # Quando i legami sono completi, mostra il lampo
    if legame1.opacity >= 0.9 and not lampo.visible:
        lampo.visible = True
        lampo.radius = 0.5
        lampo.color = color.white
        lampo.opacity = 0.9

    # Dopo il lampo, la molecola ruota lentamente
    if lampo.visible:
        ossigeno.rotate(angle=0.01, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
        idrogeno1.rotate(angle=0.01, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
        idrogeno2.rotate(angle=0.01, axis=vector(0, 1, 0), origin=vector(0, 0, 0))