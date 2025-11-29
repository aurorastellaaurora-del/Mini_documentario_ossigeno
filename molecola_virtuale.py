import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Coordinate degli atomi nella molecola d'acqua (forma tetraedrica distorta)
# O al centro, H1 e H2 legati covalentemente, H3 simulato per legame a idrogeno
O = np.array([0, 0, 0])
H1 = np.array([0.9572, 0, 0])
H2 = np.array([-0.239, 0.927, 0])
H3 = np.array([1.5, 1.5, 0])  # Idrogeno di una seconda molecola (legame a idrogeno)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.title("Molecola d'acqua (H₂O) con legame a idrogeno")

# Plot degli atomi
ax.scatter(*O, color='red', s=300, label='Ossigeno')
ax.scatter(*H1, color='blue', s=200, label='Idrogeno 1')
ax.scatter(*H2, color='blue', s=200, label='Idrogeno 2')
ax.scatter(*H3, color='blue', s=200, label='Idrogeno esterno')

# Legami covalenti
ax.plot([O[0], H1[0]], [O[1], H1[1]], [O[2], H1[2]], color='black', linewidth=2)
ax.plot([O[0], H2[0]], [O[1], H2[1]], [O[2], H2[2]], color='black', linewidth=2)

# Legame a idrogeno (tratteggiato)
ax.plot([O[0], H3[0]], [O[1], H3[1]], [O[2], H3[2]], color='gray', linestyle='dashed', linewidth=1.5)

# Etichette
ax.text(*O, 'O', fontsize=12, color='red')
ax.text(*H1, 'H', fontsize=12, color='blue')
ax.text(*H2, 'H', fontsize=12, color='blue')
ax.text(*H3, 'H (legame)', fontsize=10, color='blue')

# Impostazioni grafiche
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.tight_layout()
plt.show()