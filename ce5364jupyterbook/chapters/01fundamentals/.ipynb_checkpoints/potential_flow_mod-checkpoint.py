from dataclasses import dataclass
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

@dataclass
class GridSpec:
    deltax: float
    deltay: float
    deltaz: float
    nrows: int
    ncols: int
    distancex: np.ndarray
    distancey: np.ndarray

@dataclass
class Boundaries:
    top: np.ndarray
    bottom: np.ndarray
    left: np.ndarray
    right: np.ndarray

@dataclass
class ModelData:
    grid: GridSpec
    bounds: Boundaries
    head0: np.ndarray
    Kx: np.ndarray
    Ky: np.ndarray
    tolerance: float
    maxiter: int

def read_potential_input(path: str) -> ModelData:
    with open(path, "r") as f:
        deltax = float(f.readline().strip())
        deltay = float(f.readline().strip())
        deltaz = float(f.readline().strip())
        nrows = int(f.readline().strip())
        ncols = int(f.readline().strip())
        tolerance = float(f.readline().strip())
        maxiter = int(f.readline().strip())

        distancex = np.array([float(x) for x in f.readline().strip().split()], dtype=float)
        distancey = np.array([float(y) for y in f.readline().strip().split()], dtype=float)

        boundarytop = np.array([float(v) for v in f.readline().strip().split()], dtype=float)
        boundarybottom = np.array([int(v) for v in f.readline().strip().split()], dtype=int)
        boundaryleft = np.array([int(v) for v in f.readline().strip().split()], dtype=int)
        boundaryright = np.array([int(v) for v in f.readline().strip().split()], dtype=int)

        head0 = np.zeros((nrows, ncols), dtype=float)
        for i in range(nrows):
            head0[i, :] = np.array([float(v) for v in f.readline().strip().split()], dtype=float)

        Kx = np.zeros((nrows, ncols), dtype=float)
        for i in range(nrows):
            Kx[i, :] = np.array([float(v) for v in f.readline().strip().split()], dtype=float)

        Ky = np.zeros((nrows, ncols), dtype=float)
        for i in range(nrows):
            Ky[i, :] = np.array([float(v) for v in f.readline().strip().split()], dtype=float)

    grid = GridSpec(deltax, deltay, deltaz, nrows, ncols, distancex, distancey)
    bounds = Boundaries(boundarytop, boundarybottom, boundaryleft, boundaryright)
    return ModelData(grid, bounds, head0, Kx, Ky, tolerance, maxiter)

def assemble_coefficients(Kx: np.ndarray, Ky: np.ndarray, grid: GridSpec):
    nr, nc = grid.nrows, grid.ncols
    A = np.zeros((nr, nc), dtype=float)
    B = np.zeros((nr, nc), dtype=float)
    C = np.zeros((nr, nc), dtype=float)
    D = np.zeros((nr, nc), dtype=float)
    dx2 = grid.deltax ** 2
    dy2 = grid.deltay ** 2
    dz = grid.deltaz
    for i in range(1, nr - 1):
        for j in range(1, nc - 1):
            A[i, j] = ((Kx[i - 1, j] + Kx[i, j]) * dz) / (2.0 * dx2)
            B[i, j] = ((Kx[i, j] + Kx[i + 1, j]) * dz) / (2.0 * dx2)
            C[i, j] = ((Ky[i, j - 1] + Ky[i, j]) * dz) / (2.0 * dy2)
            D[i, j] = ((Ky[i, j] + Ky[i, j + 1]) * dz) / (2.0 * dy2)
    return A, B, C, D

def apply_no_flow_edges(head: np.ndarray, bounds: Boundaries) -> None:
    nr, nc = head.shape
    for j in range(nc):
        if bounds.top[j] == 0:
            head[0, j] = head[1, j]
        if bounds.bottom[j] == 0:
            head[nr - 1, j] = head[nr - 2, j]
    for i in range(nr):
        if bounds.left[i] == 0:
            head[i, 0] = head[i, 1]
        if bounds.right[i] == 0:
            head[i, nc - 1] = head[i, nc - 2]

def gauss_seidel_sweep(head: np.ndarray, A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray) -> None:
    nr, nc = head.shape
    for i in range(1, nr - 1):
        for j in range(1, nc - 1):
            wsum = A[i, j] + B[i, j] + C[i, j] + D[i, j]
            if wsum > 0.0:
                head[i, j] = (
                    A[i, j] * head[i - 1, j] +
                    B[i, j] * head[i + 1, j] +
                    C[i, j] * head[i, j - 1] +
                    D[i, j] * head[i, j + 1]
                ) / wsum

def solve_potential(model, verbose: bool = True):
    grid, bounds = model.grid, model.bounds
    head = model.head0.copy()
    head_old = head.copy()
    A, B, C, D = assemble_coefficients(model.Kx, model.Ky, grid)
    tol = model.tolerance
    maxiter = model.maxiter
    for it in range(1, maxiter + 1):
        apply_no_flow_edges(head, bounds)
        gauss_seidel_sweep(head, A, B, C, D)
        sse = float(np.sum((head - head_old) ** 2))
        if verbose and (it % 50 == 0 or it == 1):
            print(f"Iter {it:6d} | SSE={sse:.6e}")
        if sse <= tol:
            if verbose:
                print("Exit iterations in velocity potential because tolerance met")
                print("Iterations =", it)
            return head, it, sse
        head_old[:, :] = head
    if verbose:
        print("Reached max iterations.")
    return head, maxiter, float(np.sum((head - head_old) ** 2))

def plot_head_contours(distancex: np.ndarray, distancey: np.ndarray, head: np.ndarray,
                       title: str = "Contour Plot of Heads", nx: int = 1200, ny: int = 600, method: str = "cubic"):
    Xpts, Ypts = np.meshgrid(distancex, distancey)
    pts = np.column_stack([Xpts.ravel(), Ypts.ravel()])
    vals = head.ravel()
    gx = np.linspace(distancex.min(), distancex.max(), nx)
    gy = np.linspace(distancey.min(), distancey.max(), ny)
    GX, GY = np.meshgrid(gx, gy)
    GZ = griddata(pts, vals, (GX, GY), method=method)
    fig, ax = plt.subplots(figsize=(12, 4))
    CS = ax.contour(GX, GY, GZ, levels=10)
    ax.clabel(CS, inline=2, fontsize=12)
    ax.set_title(title)
    ax.set_xlabel("x (distance units)")
    ax.set_ylabel("y (distance units)")
    fig.tight_layout()
    return fig