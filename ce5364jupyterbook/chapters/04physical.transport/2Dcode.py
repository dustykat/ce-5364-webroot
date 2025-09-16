import numpy as np
import matplotlib.pyplot as plt

# =========================
# 2-D UPWIND ADVECTION
# =========================
def upwind_2d(
    C0: np.ndarray,        # shape (ny, nx) at t=0
    u, v,                  # scalar | (ny,nx) | (nt,) | (nt,ny,nx)
    dx: float, dy: float,
    dt: float, nt: int,
    C_left=None,           # Dirichlet at x=0: scalar | (ny,) | (nt+1,ny) | (nt,ny)
    C_right=None,          # Dirichlet at x=Lx; None => outflow
    C_bottom=None,         # Dirichlet at y=0: scalar | (nx,) | (nt+1,nx) | (nt,nx)
    C_top=None             # Dirichlet at y=Ly; None => outflow
) -> np.ndarray:
    """
    First-order upwind (Godunov) scheme in 2-D, explicit time-stepping.

    Conservative form:
        C^{n+1}_{j,i} = C^n_{j,i}
            + (dt/dx) * (F_x[j, i-1] - F_x[j, i])
            + (dt/dy) * (F_y[j-1, i] - F_y[j, i])

    Face fluxes (flux-splitting):
        F_x[j, i] = max(u_face[j,i], 0)*C[j, i] + min(u_face[j,i], 0)*C[j, i+1]
        F_y[j, i] = max(v_face[j,i], 0)*C[j, i] + min(v_face[j,i], 0)*C[j+1, i]

    where i indexes x (columns), j indexes y (rows).
    u_face has shape (ny, nx-1) on x-interfaces; v_face has shape (ny-1, nx) on y-interfaces.

    Velocity inputs u, v:
      - scalar: constant everywhere
      - (ny,nx): spatially varying, constant in time
      - (nt,): time-varying, uniform in space
      - (nt,ny,nx): fully varying in space & time
    u, v are treated as **cell-centered**; face velocities are arithmetic averages.

    Boundary conditions:
      - Left/Bottom default: Dirichlet, held to initial boundary values
      - Right/Top default: outflow (zero-gradient)

    Returns
    -------
    C : array, shape (nt+1, ny, nx)
        Concentration field over time, including t=0.
    """
    C0 = np.asarray(C0, dtype=float)
    ny, nx = C0.shape
    if ny < 2 or nx < 2:
        raise ValueError("C0 must be at least 2x2.")

    u_arr = _broadcast_vel_2d(u, nt, ny, nx)
    v_arr = _broadcast_vel_2d(v, nt, ny, nx)

    # Expand boundary condition time series
    left_series   = _expand_edge_bc(C_left,   nt, ny, default=C0[:, 0])   # (nt+1, ny)
    right_series  = _expand_edge_bc(C_right,  nt, ny, default=None)       # None => outflow
    bottom_series = _expand_edge_bc(C_bottom, nt, nx, default=C0[0, :])   # (nt+1, nx)
    top_series    = _expand_edge_bc(C_top,    nt, nx, default=None)       # None => outflow

    # CFL check: conservative 2-D explicit condition  max(|u|*dt/dx + |v|*dt/dy) <= 1
    umax = np.nanmax(np.abs(u_arr))
    vmax = np.nanmax(np.abs(v_arr))
    if (umax > 0 or vmax > 0):
        cfl = (umax * dt / dx) + (vmax * dt / dy)
        if cfl > 1.0 + 1e-12:
            print(f"⚠️ CFL warning: max(|u|*dt/dx + |v|*dt/dy) = {cfl:.3f} > 1. "
                  "Reduce dt or refine grid.")

    # Allocate solution
    C = np.zeros((nt+1, ny, nx), dtype=float)
    C[0] = C0

    for n in range(nt):
        # -- Apply BCs at current time level BEFORE fluxes --
        # Left (Dirichlet) or hold; Right (outflow unless Dirichlet)
        if left_series is not None:
            C[n, :, 0] = left_series[n]
        if right_series is None:
            C[n, :, -1] = C[n, :, -2]   # outflow
        else:
            C[n, :, -1] = right_series[n]

        # Bottom (Dirichlet) or hold; Top (outflow unless Dirichlet)
        if bottom_series is not None:
            C[n, 0, :] = bottom_series[n]
        if top_series is None:
            C[n, -1, :] = C[n, -2, :]   # outflow
        else:
            C[n, -1, :] = top_series[n]

        # -- Face velocities (cell-centered -> face-centered by averaging) --
        u_n = u_arr[n]  # (ny, nx)
        v_n = v_arr[n]  # (ny, nx)
        u_face = 0.5 * (u_n[:, :-1] + u_n[:, 1:])  # (ny, nx-1), x-interfaces
        v_face = 0.5 * (v_n[:-1, :] + v_n[1:, :])  # (ny-1, nx), y-interfaces

        # -- Fluxes --
        Fx = np.maximum(u_face, 0.0) * C[n, :, :-1] + np.minimum(u_face, 0.0) * C[n, :, 1:]
        Fy = np.maximum(v_face, 0.0) * C[n, :-1, :] + np.minimum(v_face, 0.0) * C[n, 1:, :]

        # -- Update interior cells (vectorized) --
        C[n+1, 1:-1, 1:-1] = (
            C[n, 1:-1, 1:-1]
            + (dt/dx) * (Fx[1:-1, :-1] - Fx[1:-1, 1:])
            + (dt/dy) * (Fy[:-1, 1:-1] - Fy[1:, 1:-1])
        )

        # -- Next-time BCs --
        if left_series is not None:
            C[n+1, :, 0] = left_series[n+1]
        if right_series is None:
            C[n+1, :, -1] = C[n+1, :, -2]
        else:
            C[n+1, :, -1] = right_series[n+1]

        if bottom_series is not None:
            C[n+1, 0, :] = bottom_series[n+1]
        if top_series is None:
            C[n+1, -1, :] = C[n+1, -2, :]
        else:
            C[n+1, -1, :] = top_series[n+1]

    return C


# ---------- Helpers ----------

def _broadcast_vel_2d(v, nt, ny, nx):
    """
    Broadcast v to shape (nt, ny, nx).
    Accepts: scalar | (ny,nx) | (nt,) | (nt,ny,nx)
    """
    if np.isscalar(v):
        return np.full((nt, ny, nx), float(v))
    v = np.asarray(v, dtype=float)
    if v.ndim == 2 and v.shape == (ny, nx):
        return np.repeat(v[np.newaxis, :, :], nt, axis=0)
    if v.ndim == 1 and v.size == nt:
        return np.repeat(v[:, np.newaxis, np.newaxis], ny, axis=1).repeat(nx, axis=2)
    if v.ndim == 3 and v.shape == (nt, ny, nx):
        return v
    raise ValueError("Velocity must be scalar, (ny,nx), (nt,), or (nt,ny,nx).")


def _expand_edge_bc(bc, nt, nedge, default=None):
    """
    Expand an edge Dirichlet BC to (nt+1, nedge).
    - bc=None:
        * if default is None -> return None (signals outflow)
        * else -> return constant array set to default values
    - bc scalar -> constant in time/space
    - bc 1D (nedge,) -> constant in time, varies along edge
    - bc 2D (nt,) or (nt+1,) -> uniform along edge over time
    - bc 2D (nt+1, nedge) or (nt, nedge) -> full specification
    """
    if bc is None:
        if default is None:
            return None
        default = np.asarray(default, dtype=float).ravel()
        if default.size != nedge:
            # Allow scalar default
            if default.size == 1:
                default = np.full(nedge, float(default))
            else:
                raise ValueError("Default BC length mismatch.")
        return np.repeat(default[np.newaxis, :], nt+1, axis=0)

    if np.isscalar(bc):
        arr = np.full((nt+1, nedge), float(bc))
        return arr

    bc = np.asarray(bc, dtype=float)
    # (nedge,) -> replicate over time
    if bc.ndim == 1 and bc.size == nedge:
        return np.repeat(bc[np.newaxis, :], nt+1, axis=0)

    # (nt,) or (nt+1,) -> uniform along edge over time
    if bc.ndim == 1 and (bc.size == nt or bc.size == nt+1):
        series = bc if bc.size == nt+1 else np.concatenate([bc, bc[-1:]])
        return np.repeat(series[:, np.newaxis], nedge, axis=1)

    # (nt, nedge) or (nt+1, nedge)
    if bc.ndim == 2 and bc.shape in [(nt, nedge), (nt+1, nedge)]:
        return bc if bc.shape[0] == nt+1 else np.vstack([bc, bc[-1:, :]])

    raise ValueError("Unsupported BC shape; see docstring for allowed forms.")


# =========================
# PLOTTING (contour at time t)
# =========================
def plot_contour_at_time(C, x, y, t_req, dt, levels=20, filled=True, ax=None, title=None):
    """
    Contour (or filled contour) of C(x,y,t) at the requested physical time.
    C shape: (nt+1, ny, nx); x: (nx,), y: (ny,)
    """
    C = np.asarray(C)
    y = np.asarray(y); x = np.asarray(x)
    nt = C.shape[0]-1

    k = int(round(t_req / dt))
    k = max(0, min(nt, k))
    t_used = k * dt

    if ax is None:
        fig, ax = plt.subplots(figsize=(6.5, 5.0))

    X, Y = np.meshgrid(x, y)
    if filled:
        cs = ax.contourf(X, Y, C[k], levels=levels)
    else:
        cs = ax.contour(X, Y, C[k], levels=levels)
    cbar = plt.colorbar(cs, ax=ax)
    cbar.set_label("C")

    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title(title or f"C(x,y,t) at t ≈ {t_used:.3g}")
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, alpha=0.2)
    plt.tight_layout()
    return ax, t_used, k


# Grid
nx, ny = 121, 81
x = np.linspace(0.0, 1.0, nx)
y = np.linspace(0.0, 1.0, ny)
dx = x[1]-x[0]; dy = y[1]-y[0]

# Initial condition: 2-D rectangular patch
X, Y = np.meshgrid(x, y)
C0 = ((0.2 <= X) & (X <= 0.35) & (0.4 <= Y) & (Y <= 0.6)).astype(float)

# Velocities (cell-centered); constants here
u = 1.0
v = 0.5

# Time step from conservative 2-D CFL: |u|*dt/dx + |v|*dt/dy <= 1
CFL = 0.6
dt = CFL / (abs(u)/dx + abs(v)/dy)
nt = 250

# Left & bottom Dirichlet (hold at initial boundary); right & top: outflow
C = upwind_2d(C0, u, v, dx, dy, dt, nt,
              C_left=None, C_right=None, C_bottom=None, C_top=None)

# Plot at selected times
_ = plot_contour_at_time(C, x, y, t_req=0.0,   dt=dt, levels=20, filled=True, title="t=0.0")
_ = plot_contour_at_time(C, x, y, t_req=0.25,  dt=dt, levels=20, filled=True, title="t≈0.25")
_ = plot_contour_at_time(C, x, y, t_req=0.50,  dt=dt, levels=20, filled=True, title="t≈0.50")
