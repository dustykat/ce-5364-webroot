---
title: Derivation Sketch — Advection–Dispersion with Reactions, Sorption, and Sources/Sinks
---

We assume a saturated medium with constant fluid density and porosity over the time scales of interest. The velocity field is obtained from an appropriate groundwater flow solution.

## 1) Variables and constitutive pieces

- $C(\mathbf{x},t)$ — dissolved concentration $[M\,L^{-3}]$ in the mobile (water) phase  
- $s(\mathbf{x},t)$ — sorbed concentration on the solid phase $[M\,M^{-1}]$  
- $n$ — porosity $[-]$; $\ \rho_b$ — bulk density of porous medium $[M\,L^{-3}]$  
- $\mathbf{q}$ — Darcy flux (specific discharge) $[L\,T^{-1}]$  
- $\mathbf{v}=\mathbf{q}/n$ — average linear (pore) velocity $[L\,T^{-1}]$  
- $\boldsymbol{D}$ — hydrodynamic dispersion tensor $[L^{2}\,T^{-1}]$:
  $$
  \boldsymbol{D} \;=\; \tau D_m\,\mathbf{I}
  \;+\; \alpha_T\,\lVert\mathbf{v}\rVert\,\mathbf{I}
  \;+\; (\alpha_L-\alpha_T)\,\frac{\mathbf{v}\mathbf{v}^{\!\top}}{\lVert\mathbf{v}\rVert}
  $$
  where $D_m$ is molecular diffusion, $\tau$ is tortuosity, and $\alpha_L,\alpha_T$ are longitudinal/transverse dispersivities.  
- $W(\mathbf{x},t)$ — volumetric water source/sink per bulk volume $[T^{-1}]$ (positive = water addition)  
- $C_{\mathrm{in}}(\mathbf{x},t)$ — concentration of water added through $W>0$

**Dissolved mass flux** (dispersion + advection):
$$
\mathbf{J} \;=\; -\,n\,\boldsymbol{D}\,\nabla C \;+\; \mathbf{q}\,C
\qquad [M\,L^{-2}\,T^{-1}].
$$

## 2) Species mass balance over a representative elementary volume (REV)

**Total species mass per bulk volume:**
$$
M \;=\; nC \;+\; \rho_b s.
$$

**Conservation of mass** (accumulation = inflow $-$ outflow $+$ reactions $+$ external additions):
$$
\frac{\partial}{\partial t}\big(nC + \rho_b s\big)
\;+\; \nabla\!\cdot\mathbf{J}
\;=\; nW\,C_{\mathrm{in}} \;+\; R_{\text{chem}}(C,s,\ldots),
$$
where $R_{\text{chem}}$ $[M\,L^{-3}\,T^{-1}]$ is net internal production/consumption from reactions not otherwise represented (e.g., multispecies kinetics, biodegradation).

Insert $\mathbf{J}$:
$$
\frac{\partial}{\partial t}\big(nC + \rho_b s\big)
\;+\; \nabla\!\cdot\!\big(-\,n\boldsymbol{D}\nabla C + \mathbf{q}C\big)
\;=\; nW\,C_{\mathrm{in}} \;+\; R_{\text{chem}}.
$$

> Using groundwater continuity, $\nabla\!\cdot\mathbf{q}=nW$, we have  
> $-\nabla\!\cdot(\mathbf{q}C)= -\mathbf{q}\!\cdot\nabla C \;-\; C\,\nabla\!\cdot\mathbf{q} = -\mathbf{q}\!\cdot\nabla C - nW\,C$.  
> Together with $+\,nW\,C_{\mathrm{in}}$, the net water exchange term is $nW(C_{\mathrm{in}}-C)$.

## 3) Sorption and retardation

### (a) Instantaneous linear equilibrium sorption
Assume $s = K_d\,C$. Then
$$
\frac{\partial}{\partial t}(nC + \rho_b s)
= \big(n + \rho_b K_d\big)\,\frac{\partial C}{\partial t}
= n\,R_f\,\frac{\partial C}{\partial t},
\qquad
R_f \equiv 1 + \frac{\rho_b K_d}{n}.
$$

Substitute into the balance equation above:
$$
nR_f\,\frac{\partial C}{\partial t}
= \nabla\!\cdot\!\big(n\boldsymbol{D}\nabla C\big)
- \nabla\!\cdot(\mathbf{q}C)
+ nW\,C_{\mathrm{in}}
+ R_{\text{chem}}(C)
- \lambda\,nC,
$$
where $-\lambda n C$ represents first-order aqueous decay (optional).

Divide by $n$ and use $\mathbf{v}=\mathbf{q}/n$ if preferred:
$$
R_f\,\frac{\partial C}{\partial t}
= \nabla\!\cdot\!\big(\boldsymbol{D}\nabla C\big)
- \nabla\!\cdot(\mathbf{v}C)
+ W\,C_{\mathrm{in}}
+ \frac{R_{\text{chem}}}{n}
- \lambda\,C.
$$

### (b) Kinetic sorption (first-order two-rate; optional)
Replace $s=K_d C$ with
$$
\rho_b\frac{\partial s}{\partial t}
= k_a\,\rho_b C \;-\; k_d\,\rho_b s,
$$
and keep $\rho_b \,\partial s/\partial t$ explicitly in the accumulation term. No single $R_f$ applies; this yields a coupled PDE–ODE system.

### (c) Dual-porosity / mobile–immobile (optional)
Let $n = n_m + n_{im}$ and introduce $C_{im}$:
$$
\begin{aligned}
& n_m\frac{\partial C}{\partial t} + \rho_b\frac{\partial s}{\partial t}
\;-\; \nabla\!\cdot\!\big(n_m\boldsymbol{D}\nabla C\big)
+ \nabla\!\cdot(\mathbf{q}C)
= nW\,C_{\mathrm{in}} + R_{\text{chem}} - \omega\,(C_{im}-C) - \lambda\,n_m C, \\[4pt]
& n_{im}\frac{\partial C_{im}}{\partial t}
= \omega\,(C_{im}-C) - \lambda_{im}\,n_{im} C_{im}.
\end{aligned}
$$

## 4) Canonical forms (for direct use)

**General conservative form (no assumption on sorption kinetics):**
$$
\frac{\partial}{\partial t}\big(nC + \rho_b s\big)
= \nabla\!\cdot\!\big(n\boldsymbol{D}\nabla C\big)
- \nabla\!\cdot(\mathbf{q}C)
+ nW\,C_{\mathrm{in}}
+ R_{\text{chem}}(C,s,\ldots)
- \lambda\,nC.
$$

**Retarded ADE with first-order decay (instantaneous linear sorption):**
$$
nR_f\,\frac{\partial C}{\partial t}
= \nabla\!\cdot\!\big(n\boldsymbol{D}\nabla C\big)
- \nabla\!\cdot(\mathbf{q}C)
+ nW\,C_{\mathrm{in}}
+ R_{\text{chem}}(C)
- \lambda\,nC.
$$

(Optionally divide by $n$ and write in terms of $\mathbf{v}=\mathbf{q}/n$.)

## 5) Boundary conditions (quick reference)

- **Dirichlet (specified concentration):** $C = C_b$ on $\Gamma_D$.  
- **Neumann (specified mass flux):** $\mathbf{n}\!\cdot\!\big(-n\boldsymbol{D}\nabla C + \mathbf{q}C\big) = J_b$ on $\Gamma_N$.  
- **No-flux:** $\mathbf{n}\!\cdot\!\big(-n\boldsymbol{D}\nabla C + \mathbf{q}C\big)=0$.

## 6) Units and sign checks

- $\nabla\!\cdot(n\boldsymbol{D}\nabla C)$ and $-\nabla\!\cdot(\mathbf{q}C)$ both have units $[M\,L^{-3}\,T^{-1}]$.  
- $nW(C_{\mathrm{in}}-C)$ has units $[M\,L^{-3}\,T^{-1}]$.  
- Positive $W$ adds water and mass; negative $W$ removes them.

> Notes.  
> (i) If density varies or saturation changes, retain $\rho$ and use the appropriate flow equation (e.g., Richards’ equation) and variable-density transport.  
> (ii) Spatially variable $n(\mathbf{x})$ can be kept inside divergences; if you divide by $n$, handle $\nabla n$ terms consistently.
