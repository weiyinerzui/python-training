# diffusion.py
def heat_diffusion(u, D, dt, dx):
    # Vectorized diffusion algorithm
    u[1:-1, 1:-1] = u[1:-1, 1:-1] + D * dt / dx**2 * (
        u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2] +
        u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]
    )
    return u