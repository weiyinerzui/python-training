from diffusion import heat_diffusion
import numpy as np
import matplotlib.pyplot as plt

def plt_result(u):
    plt.imshow(u, cmap='hot',interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    # Initialize parameters and call heat_diffusion
    u = np.zeros((100, 100))
    D = 0.1
    dt = 0.01
    dx = 0.1
    u = heat_diffusion(u, D ,dt, dx)
    plt_result(u)


 
