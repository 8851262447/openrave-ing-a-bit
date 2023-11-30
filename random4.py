import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.0, -2.5)),
    (Path.CURVE4, (0.2, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.3, 1.9)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.3, 3.4)),
    (Path.CURVE4, (2.8, 0.09)),
    (Path.CURVE4, (1.9, -1.05)),
    (Path.CLOSEPOLY, (1.0, -2.5)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)


x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')

ax.grid()
ax.axis('equal')
plt.show()