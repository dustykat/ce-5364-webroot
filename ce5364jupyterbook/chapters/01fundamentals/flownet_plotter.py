import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from matplotlib.lines import Line2D
import argparse
import os

def read_xyz(path):
    """
    Read an XYZ file with 3 columns: x, y, value.
    Delimiters may be commas or whitespace.
    Lines starting with '#' or '//' are ignored.
    Returns: (x, y, z) as 1D numpy arrays.
    """
    xs, ys, zs = [], [], []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            if s.startswith('#') or s.startswith('//'):
                continue
            s = s.replace(',', ' ')
            parts = s.split()
            if len(parts) < 3:
                continue
            try:
                x, y, z = float(parts[0]), float(parts[1]), float(parts[2])
            except ValueError:
                continue
            xs.append(x); ys.append(y); zs.append(z)
    if len(xs) == 0:
        raise ValueError(f"No valid data found in {path}")
    return np.asarray(xs), np.asarray(ys), np.asarray(zs)

def grid_xyz(x, y, z, nx=1200, ny=600, extent=None, method='cubic'):
    """
    Grid scattered (x,y,z) onto a regular mesh using scipy.griddata.
    extent: (xmin, xmax, ymin, ymax); if None, computed from data.
    Returns: GX, GY, GZ
    """
    if extent is None:
        xmin, xmax = np.min(x), np.max(x)
        ymin, ymax = np.min(y), np.max(y)
    else:
        xmin, xmax, ymin, ymax = extent

    gx = np.linspace(xmin, xmax, nx)
    gy = np.linspace(ymin, ymax, ny)
    GX, GY = np.meshgrid(gx, gy)

    pts = np.column_stack([x, y])
    GZ = griddata(pts, z, (GX, GY), method=method)
    return GX, GY, GZ

"""def write_xyz_grid(distancex, distancey, array2d, path):
"""
   # Helper to write a regular grid (distancex, distancey, array) into
   # 3-column XYZ format. Each row: x y value
"""
    X, Y = np.meshgrid(distancex, distancey)
    xyz = np.column_stack([X.ravel(), Y.ravel(), array2d.ravel()])
    print("in write xyz")
    np.savetxt(
        path,
        xyz,
        fmt="%.6g",
        delimiter=" ",
        header="x y value",   # do NOT include '\n' here
        comments="# "        # keeps a normal '# ' header line
    )

    
with open(path, 'w', encoding='utf-8') as f:
        f.write('# x y value')
        for i, yy in enumerate(distancey):
            for j, xx in enumerate(distancex):
                f.write(f"{xx} {yy} {array2d[i, j]}"+"\n")
"""

def write_xyz_grid(distancex, distancey, array2d, path,
                   label="value", precision=6, transpose=False,
                   newline="\n", verbose=False):
    """
    Write a regular grid to 3-column XYZ text: x y <label>

    - distancex: (ncols,)
    - distancey: (nrows,)
    - array2d:   (nrows, ncols)
    - transpose=True if your array orientation needs flipping
    """
    X, Y = np.meshgrid(distancex, distancey)
    Z = array2d.T if transpose else array2d
    xyz = np.column_stack([X.ravel(), Y.ravel(), Z.ravel()])

    np.savetxt(
        path,
        xyz,
        fmt=f"%.{precision}g",
        delimiter=" ",
        header=f"x y {label}",   # reader ignores '#' lines
        comments="# ",
        newline=newline          # ensures real newlines on all OSes
    )
    if verbose:
        print(f"Wrote {xyz.shape[0]} rows to {path}")

def plot_flownet(head_file, stream_file,
                 head_levels=None, stream_levels=None,
                 nx=1200, ny=600, method='cubic',
                 title='Flownet', figsize=(7.5, 4),
                 head_label_size=12, stream_label_size=10,
                 save_png=None, transparent=True):
    """
    Plot head and stream-function contours from two XYZ files on a common grid.

    Parameters
    ----------
    head_file : str
        Path to XYZ file with (x, y, head).
    stream_file : str
        Path to XYZ file with (x, y, stream function).
    head_levels : list[float] or None
        Contour levels for head. If None, auto-selected.
    stream_levels : list[float] or None
        Contour levels for stream function. If None, auto-selected.
    nx, ny : int
        Grid size for interpolation.
    method : str
        'nearest', 'linear', or 'cubic' interpolation.
    title : str
        Figure title.
    figsize : tuple
        Figure size in inches.
    head_label_size, stream_label_size : int
        Font sizes for contour labels.
    save_png : str or None
        If provided, save to this path.
    transparent : bool
        Save PNG with transparent background.

    Returns
    -------
    fig : matplotlib.figure.Figure
    ax : matplotlib.axes.Axes
    """
    x1, y1, z1 = read_xyz(head_file)
    x2, y2, z2 = read_xyz(stream_file)

    # Common extent from union of both datasets
    xmin = min(np.min(x1), np.min(x2))
    xmax = max(np.max(x1), np.max(x2))
    ymin = min(np.min(y1), np.min(y2))
    ymax = max(np.max(y1), np.max(y2))
    extent = (xmin, xmax, ymin, ymax)

    # Grid both to the same mesh
    GX, GY, GZ1 = grid_xyz(x1, y1, z1, nx=nx, ny=ny, extent=extent, method=method)
    _,  _,  GZ2 = grid_xyz(x2, y2, z2, nx=nx, ny=ny, extent=extent, method=method)

    # Auto levels if not provided
    def auto_levels(arr, n=10):
        finite = np.asarray(arr[np.isfinite(arr)])
        if finite.size == 0:
            return None
        lo, hi = np.percentile(finite, [10, 90]) if np.ptp(finite) > 0 else (finite.min(), finite.max())
        if hi == lo:
            hi = lo + 1.0  # avoid degenerate contour
        return np.linspace(lo, hi, n)

    if head_levels is None:
        head_levels = auto_levels(GZ1, n=8)
    if stream_levels is None:
        stream_levels = auto_levels(GZ2, n=10)

    fig, ax = plt.subplots(figsize=figsize)

    # Head: solid lines
    CS1 = ax.contour(GX, GY, GZ1, levels=head_levels)
    ax.clabel(CS1, inline=2, fontsize=head_label_size)

    # Stream function: dashed lines (no explicit color set)
    CS2 = ax.contour(GX, GY, GZ2, levels=stream_levels, linestyles='--')
    ax.clabel(CS2, inline=2, fontsize=stream_label_size)

    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Legend using proxy artists (default line color, different linestyles)
    proxies = [
        Line2D([0], [0]),
        Line2D([0], [0], linestyle='--')
    ]
    ax.legend(proxies, ['Potential function (head)', 'Stream function (streamlines)'], loc='best', frameon=True)

    ax.set_aspect('equal', adjustable='box')  # force 1:1 scale in x and y
    fig.tight_layout()

    if save_png:
        fig.savefig(save_png, dpi=300, bbox_inches='tight', transparent=transparent)

    return fig, ax

def _parse_levels(s):
    """Parse a comma-separated string of numbers into a list of floats."""
    if s is None:
        return None
    s = s.strip()
    if not s:
        return None
    return [float(x) for x in s.split(',')]

def main():
    parser = argparse.ArgumentParser(description='Flownet plotter: overlay head and stream function contours.')
    parser.add_argument('head_file', help='Path to head XYZ file (x y head).')
    parser.add_argument('stream_file', help='Path to stream-function XYZ file (x y psi).')
    parser.add_argument('--levels-head', type=str, default=None, help='Comma-separated head contour levels, e.g., "5,6,7,8".')
    parser.add_argument('--levels-stream', type=str, default=None, help='Comma-separated stream contour levels, e.g., "10,20,30".')
    parser.add_argument('--nx', type=int, default=1200, help='Interpolation grid size in x.')
    parser.add_argument('--ny', type=int, default=600, help='Interpolation grid size in y.')
    parser.add_argument('--method', type=str, default='cubic', choices=['nearest','linear','cubic'], help='griddata method.')
    parser.add_argument('--title', type=str, default='Flownet', help='Figure title.')
    parser.add_argument('--save', type=str, default=None, help='Output PNG path.')
    parser.add_argument('--transparent', action='store_true', help='Save with transparent background.')
    args = parser.parse_args()

    fig, ax = plot_flownet(
        args.head_file, args.stream_file,
        head_levels=_parse_levels(args.levels_head),
        stream_levels=_parse_levels(args.levels_stream),
        nx=args.nx, ny=args.ny, method=args.method,
        title=args.title, save_png=args.save, transparent=args.transparent
    )
    plt.show()

if __name__ == '__main__':
    main()