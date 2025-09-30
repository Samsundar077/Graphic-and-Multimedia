[0, sy, 0, 0],
 [0, 0, sz, 0],
 [0, 0, 0, 1]])
def rotation_matrix_z(angle):
 rad = np.radians(angle)
 return np.array([[np.cos(rad), -np.sin(rad), 0, 0],
 [np.sin(rad), np.cos(rad), 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1]])
def apply_transform(vertices, matrix):
 transformed = []
 for v in vertices:
 vec = np.array([*v, 1])
 result = matrix @ vec
 transformed.append(result[:3])
 return transformed
# Define Cube
vertices = [(0,0,0), (1,0,0), (1,1,0), (0,1,0),
 (0,0,1), (1,0,1), (1,1,1), (0,1,1)]
edges = [(0,1),(1,2),(2,3),(3,0),
 (4,5),(5,6),(6,7),(7,4),
 (0,4),(1,5),(2,6),(3,7)]
# Apply transformations
T = translation_matrix(2, 2, 0)
S = scaling_matrix(1.5, 1.5, 1.5)
R = rotation_matrix_z(45)
transformed_vertices = apply_transform(vertices, T @ S @ R)
# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
draw_edges(ax, vertices, edges, 'blue') # Original cube
draw_edges(ax, transformed_vertices, edges, 'red') # Transformed cube
ax.set_title("3D Transformation of Cube")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1,1,1])
plt.show() 
