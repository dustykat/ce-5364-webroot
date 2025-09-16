import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

def make_site_map(
    xlim=(0, 100),
    ylim=(0, 100),
    points=None,
    rectangles=None,
    polygons=None,
    labels=None,
    title="Site Map (Annotated Scatterplot)",
    grid=True,
    grid_spacing=None,
    equal_aspect=True,
    invert_y=False,
    dpi=300,
    outfile_png="site_map.png",
    transparent=True,
):
    if points is None: points = []
    if rectangles is None: rectangles = []
    if polygons is None: polygons = []
    if labels is None: labels = {'fontsize': 10, 'offset': (1.5, 1.5)}
    fs = labels.get('fontsize', 10)
    dx, dy = labels.get('offset', (1.5, 1.5))

    fig, ax = plt.subplots(figsize=(8, 6))

    for p in points:
        x, y = p['x'], p['y']
        marker = p.get('marker', 'o')
        size = p.get('size', 50)
        ax.scatter([x], [y], marker=marker, s=size)
        if p.get('label') and p.get('annotate', True):
            ax.annotate(p['label'], (x, y), xytext=(x + dx, y + dy),
                        textcoords='data', fontsize=fs,
                        arrowprops=dict(arrowstyle='-', lw=0.8))

    for r in rectangles:
        xy = r['xy']; width = r['width']; height = r['height']
        lw = r.get('lw', 1.5)
        rect = Rectangle(xy, width, height, fill=False, lw=lw)
        ax.add_patch(rect)
        if r.get('label'):
            rx = xy[0] + width/2.0; ry = xy[1] + height/2.0
            ax.annotate(r['label'], (rx, ry), ha='center', va='center')

    for poly in polygons:
        xy = poly['xy']; lw = poly.get('lw', 1.5)
        closed = poly.get('closed', True)
        poly_patch = Polygon(xy, closed=closed, fill=False, lw=lw)
        ax.add_patch(poly_patch)
        if poly.get('label'):
            cx = sum(pt[0] for pt in xy)/len(xy)
            cy = sum(pt[1] for pt in xy)/len(xy)
            ax.annotate(poly['label'], (cx, cy), ha='center', va='center')

    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if equal_aspect: ax.set_aspect('equal', adjustable='box')
    if invert_y: ax.invert_yaxis()
    ax.set_title(title)

    if grid: ax.grid(True, which='both', linestyle='--', linewidth=0.6)
    if grid_spacing is not None and grid_spacing > 0:
        from matplotlib.ticker import MultipleLocator
        ax.xaxis.set_major_locator(MultipleLocator(grid_spacing))
        ax.yaxis.set_major_locator(MultipleLocator(grid_spacing))

    plt.tight_layout()
    fig.savefig(outfile_png, dpi=dpi, transparent=transparent, bbox_inches='tight')
    return fig, ax, outfile_png