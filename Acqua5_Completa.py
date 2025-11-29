# © Aurora Stella - MIT License


from vpython import *
import math
import time

# ------------------------------
# Impostazioni generali della scena
# ------------------------------
scene.background = color.black
scene.width = 1000
scene.height = 700
scene.title = "La nascita dell’acqua"
distant_light(direction=vector(1, 1, 1), color=color.white)

# Lista globale per tenere traccia degli oggetti creati in ogni scena
scene_objects = []

def register(obj):
    """Registra un oggetto così lo possiamo nascondere/elimare quando passiamo alla scena successiva."""
    scene_objects.append(obj)
    return obj

def clear_scene():
    """Nasconde e svuota tutti gli oggetti registrati (evita duplicazioni nelle scene unite)."""
    for o in scene_objects:
        try:
            o.visible = False  # nasconde l'oggetto dalla scena
        except Exception:
            pass
    scene_objects.clear()

# ------------------------------
# Funzione: Scena 1 – L’ossigeno si rivela
# ------------------------------
def scena_1():
    clear_scene()  # FIX: rimuovo gli oggetti delle eventuali scene precedenti
    ossigeno = register(sphere(pos=vector(0, 0, 0), radius=0.4, color=color.cyan, opacity=1))

    # Nucleo tipo morula
    nucleo = []
    for i in range(12):
        angolo = i * math.pi / 6
        r = 0.1
        x = r * math.cos(angolo)
        y = r * math.sin(angolo)
        z = 0.05 * math.sin(i)
        particella = register(sphere(pos=ossigeno.pos + vector(x, y, z), radius=0.05, color=color.purple, opacity=0.8))
        nucleo.append(particella)

    # Elettroni
    elettroni = []
    for i in range(6):
        angolo = i * math.pi / 3
        raggio = 0.25
        pos = ossigeno.pos + vector(raggio * math.cos(angolo), raggio * math.sin(angolo), 0)
        e = register(sphere(pos=pos, radius=0.03, color=color.yellow, emissive=True))
        elettroni.append(e)

    t0 = time.time()
    while time.time() - t0 < 10:
        rate(60)
        t = time.time() - t0

        # Rotazione ossigeno
        ossigeno.rotate(angle=0.01, axis=vector(0, 1, 0))

        # Opacità decrescente
        ossigeno.opacity = max(0.3, 1 - t / 10)

        # Orbita elettroni
        for i in range(6):
            angolo = i * math.pi / 3 + 1.5 * t
            elettroni[i].pos = ossigeno.pos + vector(0.25 * math.cos(angolo), 0.25 * math.sin(angolo), 0)

# ------------------------------
# Funzione: Scena 2 – Gli idrogeni si preparano
# ------------------------------
def scena_2():
    clear_scene()  # FIX: rimuovo gli oggetti creati prima di mostrarne di nuovi
    pos1 = vector(-1, 0.5, 0)
    pos2 = vector(1, -0.5, 0)
    idrogeno1 = register(sphere(pos=pos1, radius=0.2, color=color.red, opacity=0.5))
    idrogeno2 = register(sphere(pos=pos2, radius=0.2, color=color.red, opacity=0.5))
    protone1 = register(sphere(pos=pos1, radius=0.07, color=color.red, opacity=0.8))
    protone2 = register(sphere(pos=pos2, radius=0.07, color=color.red, opacity=0.8))
    elettrone1 = register(sphere(pos=pos1 + vector(0.25, 0, 0), radius=0.03, color=color.yellow, emissive=True))
    elettrone2 = register(sphere(pos=pos2 + vector(0.25, 0, 0), radius=0.03, color=color.yellow, emissive=True))

    t0 = time.time()
    while time.time() - t0 < 10:
        rate(60)
        t = time.time() - t0

        # Rotazioni
        idrogeno1.rotate(angle=0.01, axis=vector(0, 1, 0), origin=pos1)
        idrogeno2.rotate(angle=0.01, axis=vector(0, 1, 0), origin=pos2)

        # Orbita elettroni
        elettrone1.pos = pos1 + vector(0.25 * math.cos(2*t), 0.25 * math.sin(2*t), 0)
        elettrone2.pos = pos2 + vector(0.25 * math.cos(-2*t), 0.25 * math.sin(-2*t), 0)

# ------------------------------
# Funzione: Scena 3 – Nascita della molecola
# ------------------------------
def scena_3():
    clear_scene()  # FIX: rimuovo gli oggetti precedenti per evitare duplicazioni
    # Creo la molecola centrata esplicitamente nell'origine (ossigeno al centro)
    ossigeno = register(sphere(pos=vector(0, 0, 0), radius=0.4, color=color.cyan, opacity=1))
    idrogeno1 = register(sphere(pos=vector(-2, 0.5, 0), radius=0.2, color=color.red, opacity=1))
    idrogeno2 = register(sphere(pos=vector(2, -0.5, 0), radius=0.2, color=color.red, opacity=1))
    legame1 = register(cylinder(pos=ossigeno.pos, axis=idrogeno1.pos - ossigeno.pos, radius=0.005, color=color.orange, opacity=0.05))
    legame2 = register(cylinder(pos=ossigeno.pos, axis=idrogeno2.pos - ossigeno.pos, radius=0.005, color=color.orange, opacity=0.05))
    lampo = register(sphere(pos=ossigeno.pos, radius=0.01, color=color.white, emissive=True, visible=False))

    t0 = time.time()
    while time.time() - t0 < 10:
        rate(60)
        t = time.time() - t0

        # Avvicinamento idrogeni (fino a distanza target)
        target_dist = 0.6
        d1 = mag(idrogeno1.pos - ossigeno.pos)
        d2 = mag(idrogeno2.pos - ossigeno.pos)
        if d1 > target_dist:
            idrogeno1.pos += vector(0.02, -0.005, 0)
        if d2 > target_dist:
            idrogeno2.pos += vector(-0.02, 0.005, 0)

        # Aggiorna legami
        legame1.pos = ossigeno.pos
        legame1.axis = idrogeno1.pos - ossigeno.pos
        legame2.pos = ossigeno.pos
        legame2.axis = idrogeno2.pos - ossigeno.pos

        # Intensifica legami
        legame1.opacity = min(1, legame1.opacity + 0.01)
        legame2.opacity = min(1, legame2.opacity + 0.01)
        legame1.radius = min(0.02, legame1.radius + 0.0005)
        legame2.radius = min(0.02, legame2.radius + 0.0005)

        # Lampo finale
        if legame1.opacity >= 0.9 and not lampo.visible:
            lampo.visible = True
            lampo.radius = 0.5
            lampo.opacity = 0.9

        # Rotazione molecola dopo il lampo
        if lampo.visible:
            ossigeno.rotate(angle=0.01, axis=vector(0, 1, 0), origin=ossigeno.pos)
            idrogeno1.rotate(angle=0.01, axis=vector(0, 1, 0), origin=ossigeno.pos)
            idrogeno2.rotate(angle=0.01, axis=vector(0, 1, 0), origin=ossigeno.pos)

# ------------------------------
# Funzione: Scena 4 – Tetraedro dell’acqua
# ------------------------------
def scena_4():
    clear_scene()  # FIX: rimuovo gli oggetti precedenti per avere solo il tetraedro qui
    # Creo la molecola al centro e poi il tetraedro attorno al centro della molecola
    ossigeno = register(sphere(pos=vector(0, 0, 0), radius=0.4, color=color.cyan, opacity=1))
    idrogeno1 = register(sphere(pos=vector(0.6, 0.4, 0), radius=0.2, color=color.red, opacity=1))
    idrogeno2 = register(sphere(pos=vector(0.6, -0.4, 0), radius=0.2, color=color.red, opacity=1))
    legame1 = register(cylinder(pos=ossigeno.pos, axis=idrogeno1.pos - ossigeno.pos, radius=0.02, color=color.orange, opacity=0.8))
    legame2 = register(cylinder(pos=ossigeno.pos, axis=idrogeno2.pos - ossigeno.pos, radius=0.02, color=color.orange, opacity=0.8))

    # Vertici tetraedro centrati su ossigeno.pos (FIX: centrati correttamente)
    center = ossigeno.pos
    v1 = center + vector(0, 1, 0.7)
    v2 = center + vector(-1, -0.8, 0.7)
    v3 = center + vector(1, -0.8, 0.7)
    v4 = center + vector(0, 0, -1.2)
    vertici = [v1, v2, v3, v4]
    linee = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    curve_objs = []
    for i,j in linee:
        c = register(curve(pos=[vertici[i], vertici[j]], radius=0.01, color=color.white))
        curve_objs.append(c)

    t0 = time.time()
    while time.time() - t0 < 10:
        rate(60)
        angolo = 0.01
        asse = vector(0, 1, 0)

        # Ruota vertici attorno al centro (FIX: rotazione calcolata rispetto al centro)
        for i in range(len(vertici)):
            # sottraggo center, ruoto, poi riaggiungo center per mantenere la rotazione intorno al centro
            rel = vertici[i] - center
            rel = rel.rotate(angle=angolo, axis=asse)
            vertici[i] = center + rel

        # Aggiorna curve
        for k in range(len(linee)):
            i,j = linee[k]
            curve_objs[k].clear()
            curve_objs[k].append(vertici[i])
            curve_objs[k].append(vertici[j])

        # Ruota anche la molecola attorno al center (coerente con il tetraedro)
        ossigeno.rotate(angle=angolo, axis=asse, origin=center)
        idrogeno1.rotate(angle=angolo, axis=asse, origin=center)
        idrogeno2.rotate(angle=angolo, axis=asse, origin=center)
        legame1.pos = ossigeno.pos
        legame1.axis = idrogeno1.pos - ossigeno.pos
        legame2.pos = ossigeno.pos
        legame2.axis = idrogeno2.pos - ossigeno.pos

# ------------------------------
# Avvio sequenza completa
# ------------------------------
scena_1()
scena_2()
scena_3()
scena_4()
