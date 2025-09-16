import numpy as np

def upwind_1d(
    C0: np.ndarray,
    v,                     # scalar, (nx,), (nt,), or (nt, nx)
    dx: float,
    dt: float,
    nt: int,
    C_left=None,           # left Dirichlet BC: scalar or array length nt+1/nt
    C_right=None           # right Dirichlet BC: scalar or array length nt+1/nt
) -> np.ndarray:
    """
    First-order upwind finite-difference solver for 1D advection:
        C_i^{n+1} = C_i^n + (dt/dx) * (F_{i-1/2} - F_{i+1/2})
    with interface flux (Godunov/flux-splitting):
        F_{i+1/2} = max(v_i,0)*C_i + min(v_i,0)*C_{i+1}

    Parameters
    ----------
    C0 : (nx,) array
        Initial concentration profile at t=0.
    v : scalar | (nx,) | (nt,) | (nt,nx)
        Velocity. Interpreted at cell interfaces i = 0..nx-2 as v[i].
        - scalar: constant in space & time
        - (nx,): spatially varying, constant in time
        - (nt,): time-varying, uniform in space
        - (nt,nx): varying in space & time (uses v[n, i] at interfaces)
    dx, dt : float
        Grid spacing and time step.
    nt : int
        Number of time steps to advance.
    C_left, C_right : scalar | array | None
        Dirichlet boundary concentration at x=0 and x=L.
        If array, may be length nt or nt+1; if scalar, held constant.
        If None, defaults:
            - left: hold C[0] fixed at its initial value
            - right: zero-gradient outflow (C[-1] = C[-2] each step)

    Returns
    -------
    C : (nt+1, nx) array
        Concentration field over time (including the initial state).
    """
    C0 = np.asarray(C0, dtype=float)
    nx = C0.size
    if nx < 2:
        raise ValueError("C0 must have length >= 2.")

    # --- Broadcast velocity to shape (nt, nx) for convenience ---
    v_arr = _broadcast_velocity(v, nt, nx)

    # --- Prepare boundary series ---
    left_series  = _expand_bc(C_left,  nt, default=C0[0])
    right_series = _expand_bc(C_right, nt, default=None)  # None => outflow

    # --- CFL check (conservative, using max over provided v) ---
    vmax = np.nanmax(np.abs(v_arr))
    if vmax > 0 and (dt/dx) * vmax > 1.0 + 1e-12:
        print(f"⚠️ CFL warning: (dt/dx)*max|v| = {(dt/dx)*vmax:.3f} > 1. "
              "First-order upwind may become unstable. Consider reducing dt.")

    # --- Allocate solution ---
    C = np.zeros((nt+1, nx), dtype=float)
    C[0] = C0

    for n in range(nt):
        # Apply/hold left Dirichlet at time level n before fluxes
        C[n, 0] = left_series[n]  # if left_series is default, this holds C[0] fixed

        # Velocity at interfaces for this step: use first nx-1 entries
        v_n = v_arr[n, :]

        # Interface fluxes between i and i+1 for i = 0..nx-2
        # F[i] = flux through the interface between cell i and cell i+1
        F = np.maximum(v_n[:-1], 0.0) * C[n, :-1] + np.minimum(v_n[:-1], 0.0) * C[n, 1:]

        # Update interior cells i = 1..nx-2
        C[n+1, 1:-1] = C[n, 1:-1] + (dt/dx) * (F[:-1] - F[1:])

        # Left boundary (Dirichlet at next time)
        C[n+1, 0] = left_series[n+1]

        # Right boundary
        if right_series is None:
            # Zero-gradient (advective outflow): copy neighbor after update
            C[n+1, -1] = C[n+1, -2]
        else:
            # Dirichlet at the right boundary
            C[n+1, -1] = right_series[n+1]

    return C


# ---------- Helpers ----------

def _broadcast_velocity(v, nt, nx):
    """
    Return velocity array of shape (nt, nx).
    Interprets v[..., i] as the velocity used at interface i (between i and i+1).
    The last column (i = nx-1) is unused and may be ignored, but we keep shape uniform.
    """
    if np.isscalar(v):
        v_arr = np.full((nt, nx), float(v))
    else:
        v = np.asarray(v, dtype=float)
        if v.ndim == 1:
            if v.size == nx:
                v_arr = np.repeat(v[np.newaxis, :], nt, axis=0)
            elif v.size == nt:
                v_arr = np.repeat(v[:, np.newaxis], nx, axis=1)
            else:
                raise ValueError("v length must be nx or nt if 1D.")
        elif v.ndim == 2:
            if v.shape != (nt, nx):
                raise ValueError(f"v shape must be (nt, nx) if 2D; got {v.shape}.")
            v_arr = v
        else:
            raise ValueError("v must be scalar, 1D, or 2D.")
    return v_arr


def _expand_bc(bc, nt, default=None):
    """
    Normalize boundary condition to a series of length nt+1.
    - If bc is None: returns default behavior
        * left: return an array that repeats default (Dirichlet hold)
        * right: returns None to signal outflow handling
    - If scalar: constant BC over time
    - If array-like length nt or nt+1: broadcast to length nt+1
    """
    if bc is None:
        # left: use default value; right: signal open boundary with None
        return None if default is None else np.full(nt+1, float(default))

    if np.isscalar(bc):
        return np.full(nt+1, float(bc))

    bc = np.asarray(bc, dtype=float).ravel()
    if bc.size == nt:
        # Extend by repeating the last value
        return np.concatenate([bc, bc[-1:]])
    if bc.size == nt + 1:
        return bc

    raise ValueError("Boundary series must be scalar or length nt or nt+1.")

import numpy as np
import matplotlib.pyplot as plt

def plot_profiles(C, x, times, dt, ax=None, title="Profiles at selected times"):
    """
    Plot C(x, t) for several physical times.

    Parameters
    ----------
    C : array, shape (nt+1, nx)
        Solution including initial condition at t=0.
    x : array, shape (nx,)
        Grid coordinates.
    times : list/array of floats
        Physical times to plot (same units as dt).
    dt : float
        Time step size.
    ax : matplotlib.axes.Axes or None
        Optional axis to draw on. Creates one if None.
    title : str
        Plot title.

    Returns
    -------
    ax : matplotlib.axes.Axes
    used_times : ndarray of floats
        The actual times used (snapped to the time grid).
    used_indices : ndarray of ints
        The corresponding time indices.
    """
    C = np.asarray(C); x = np.asarray(x)
    nt = C.shape[0] - 1

    # Map requested times to nearest indices
    k_list, t_used = [], []
    for t in np.atleast_1d(times):
        k = int(round(t / dt))
        k = max(0, min(nt, k))
        k_list.append(k)
        t_used.append(k * dt)
    k_list = np.array(k_list, dtype=int)
    t_used = np.array(t_used, dtype=float)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 4.5))

    for k, tval in zip(k_list, t_used):
        ax.plot(x, C[k, :], label=f"t = {tval:.3g}")

    ax.set_xlabel("x")
    ax.set_ylabel("C")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    return ax, t_used, k_list


def plot_histories(C, x, x_locs, dt, ax=None, by="coord", title="Concentration Histories at selected locations"):
    """
    Plot C(t) at several spatial locations.

    Parameters
    ----------
    C : array, shape (nt+1, nx)
        Solution including initial condition at t=0.
    x : array, shape (nx,)
        Grid coordinates.
    x_locs : list/array
        If by='coord': physical x-locations to sample (floats).
        If by='index': integer node indices.
    dt : float
        Time step size.
    ax : matplotlib.axes.Axes or None
        Optional axis to draw on. Creates one if None.
    by : {'coord','index'}
        How to interpret x_locs.
    title : str
        Plot title.

    Returns
    -------
    ax : matplotlib.axes.Axes
    used_indices : ndarray of ints
        Grid indices actually plotted.
    """
    C = np.asarray(C); x = np.asarray(x)
    nt, nx = C.shape[0]-1, C.shape[1]
    t = np.arange(nt+1) * dt

    # Map requested locations to indices
    j_list = []
    if by == "coord":
        for x0 in np.atleast_1d(x_locs):
            j = int(np.argmin(np.abs(x - float(x0))))
            j_list.append(j)
    elif by == "index":
        for j in np.atleast_1d(x_locs):
            j_list.append(int(np.clip(int(j), 0, nx-1)))
    else:
        raise ValueError("by must be 'coord' or 'index'.")

    j_list = np.array(j_list, dtype=int)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 4.5))

    for j in j_list:
        ax.plot(t, C[:, j], label=f"x ≈ {x[j]:.3g} (j={j})")

    ax.set_xlabel("t")
    ax.set_ylabel("C")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    return ax, j_list

import numpy as np

def rectangular_pulse_centered(x, x0, width, C0=1.0):
    """
    Node-based top-hat: C(x) = C0 for |x - x0| <= width/2, else 0.
    """
    x = np.asarray(x)
    half = 0.5 * float(width)
    return C0 * ((x >= x0 - half) & (x <= x0 + half)).astype(float)

def rectangular_pulse_segment(x, x1, x2, C0=1.0):
    """
    Node-based top-hat: C(x) = C0 for x1 <= x <= x2, else 0.
    """
    x = np.asarray(x)
    lo, hi = min(x1, x2), max(x1, x2)
    return C0 * ((x >= lo) & (x <= hi)).astype(float)

def rectangular_pulse_cellavg(x, dx, x1, x2, C0=1.0):
    """
    Cell-averaged top-hat for uniform grid with centers at x and spacing dx.
    For each cell, compute overlap length with [x1, x2] and scale by C0*(overlap/dx).
    """
    x = np.asarray(x, dtype=float)
    lo, hi = min(x1, x2), max(x1, x2)
    left_edges  = x - 0.5*dx
    right_edges = x + 0.5*dx
    overlap = np.maximum(0.0, np.minimum(right_edges, hi) - np.maximum(left_edges, lo))
    return C0 * (overlap / dx)

# Grid
nx = 201
x = np.linspace(0.0, 1.0, nx)
dx = x[1] - x[0]

# Gaussian pulse centered at x0 with sd w and height C0
x0, w, C0 = 0.2, 0.025, 100.0
C_init = C0*np.exp(-((x - x0)/w)**2)   
# Rectangular pulse centered at x0 with width w and height C0
#x0, w, C0 = 0.05, 0.10, 0.0
# Option A: node-based
#C_init = rectangular_pulse_centered(x, x0, w, C0=C0)
# Option B: exact cell-average (better for narrow pulses)
# C_init = rectangular_pulse_cellavg(x, dx, x0 - w/2, x0 + w/2, C0=C0)

# Time / velocity and run
v = 1.0
dt = 0.40 * dx / abs(v)   # CFL = 0.4
nt = 300
C = upwind_1d(C_init, v, dx, dt, nt, C_left=0.0)  # uses the solver from earlier

# Plots (helpers from earlier)
_ = plot_profiles(C, x, times=[0.0, 0.2, 0.4, 0.6], dt=dt, title="Upwind formulation advection")
_ = plot_histories(C, x, x_locs=[0.0, 0.25, 0.50, 0.75], dt=dt, by="coord")

