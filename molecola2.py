import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Funzione per creare una molecola d'acqua con posizione iniziale
def crea_molecola(posizione):
    O = posizione
    # Vettori per i due idrogeni in geometria tetraedrica distorta
    H1 = posizione + np.array([0.9572, 0, 0])
    H2 = posizione + np.array([-0.239, 0.927, 0])
    return O, H1, H2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.title("Cluster di 9 molecole d'acqua con legami a idrogeno")

molecole = []

# Genera 9 molecole in una griglia 3x3
for i in range(3):
    for j in range(3):
        base = np.array([i * 3.0, j * 3.0, 0])
        O, H1, H2 = crea_molecola(base)
        molecole.append((O, H1, H2))
        # Plot atomi
        ax.scatter(*O, color='red', s=300)     # Ossigeno
        ax.scatter(*H1, color='blue', s=200)   # Idrogeno 1
        ax.scatter(*H2, color='blue', s=200)   # Idrogeno 2
        # Legami covalenti
        ax.plot([O[0], H1[0]], [O[1], H1[1]], [O[2], H1[2]], color='black', linewidth=2)
        ax.plot([O[0], H2[0]], [O[1], H2[1]], [O[2], H2[2]], color='black', linewidth=2)

# Aggiungi legami a idrogeno tra molecole vicine
for idx in range(len(molecole) - 1):
    O1 = molecole[idx][0]
    H_ext = molecole[idx + 1][1]  # Usa H1 della molecola successiva
    ax.plot([O1[0], H_ext[0]], [O1[1], H_ext[1]], [O1[2], H_ext[2]], color='gray', linestyle='dashed', linewidth=1.5)

# Impostazioni grafiche
ax.set_xlim([-1, 9])
ax.set_ylim([-1, 9])
ax.set_zlim([-1, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.show()