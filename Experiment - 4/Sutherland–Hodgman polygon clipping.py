import matplotlib.pyplot as plt

# Define clipping edges
LEFT, RIGHT, BOTTOM, TOP = range(4)

def is_inside(point, edge, clip_win):
    """Check if point is inside a clipping edge"""
    x, y = point
    xmin, xmax, ymin, ymax = clip_win
    if edge == LEFT:
        return x >= xmin
    elif edge == RIGHT:
        return x <= xmax
    elif edge == BOTTOM:
        return y >= ymin
    elif edge == TOP:
        return y <= ymax

def compute_intersection(p1, p2, edge, clip_win):
    """Find intersection of polygon edge with clipping boundary"""
    xmin, xmax, ymin, ymax = clip_win
    x1, y1 = p1
    x2, y2 = p2

    if edge == LEFT:
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
    elif edge == RIGHT:
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
    elif edge == BOTTOM:
        y = ymin
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
    elif edge == TOP:
        y = ymax
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)

    return (x, y)

def sutherland_hodgman_clip(polygon, clip_win):
    """Perform polygon clipping using Sutherland-Hodgman"""
    output_list = polygon
    for edge in [LEFT, RIGHT, BOTTOM, TOP]:
        input_list = output_list
        output_list = []
        if not input_list:
            break
        s = input_list[-1]
        for p in input_list:
            if is_inside(p, edge, clip_win):
                if not is_inside(s, edge, clip_win):
                    output_list.append(compute_intersection(s, p, edge, clip_win))
                output_list.append(p)
            elif is_inside(s, edge, clip_win):
                output_list.append(compute_intersection(s, p, edge, clip_win))
            s = p
    return output_list

def draw_polygon(points, color, label):
    """Draw polygon given a list of points"""
    x, y = zip(*(points + [points[0]]))  # close polygon
    plt.plot(x, y, color=color, label=label)

# Main
clip_window = (100, 300, 100, 300)  # xmin, xmax, ymin, ymax
polygon = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 350), (150, 300)]

# Clip polygon
clipped_polygon = sutherland_hodgman_clip(polygon, clip_window)

# Plot
plt.figure(figsize=(8, 8))
draw_polygon(polygon, 'blue', "Original Polygon")
draw_polygon(
    [(clip_window[0], clip_window[2]), (clip_window[1], clip_window[2]),
     (clip_window[1], clip_window[3]), (clip_window[0], clip_window[3])],
    'black', "Clipping Window"
)
draw_polygon(clipped_polygon, 'red', "Clipped Polygon")
plt.legend()
plt.title("Polygon Clipping using Sutherland-Hodgman Algorithm")
plt.grid(True)
plt.axis("equal")
plt.show()
