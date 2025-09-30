import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Cube vertices
verts = np.array([
    [0,0,0], [1,0,0], [1,1,0], [0,1,0],
    [0,0,1], [1,0,1], [1,1,1], [0,1,1]
])

# Faces defined by vertex indices
faces = [
    [verts[i] for i in [0,1,2,3]],  # bottom
    [verts[i] for i in [4,5,6,7]],  # top
    [verts[i] for i in [0,1,5,4]],  # front
    [verts[i] for i in [2,3,7,6]],  # back
    [verts[i] for i in [1,2,6,5]],  # right
    [verts[i] for i in [0,3,7,4]]   # left (slightly reordered vs your code)
]

# Different face colors
face_colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'orange']

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cube = Poly3DCollection(faces, facecolors=face_colors,
                        edgecolors='black', linewidths=1)
ax.add_collection3d(cube)

# Labels and appearance
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Cube with Flat Shading")
ax.set_box_aspect([1, 1, 1])  # equal aspect ratio

plt.show()
