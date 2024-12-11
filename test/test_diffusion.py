import numpy as np
import pytest
from diffusion import heat_diffusion

def test_heat_diffusion():
    u = np.zeros((10, 10))
    D = 0.1
    dt = 0.01
    dx = 0.1
    result = heat_diffusion(u, D, dt, dx)
    assert np.all(result >= 0)

if __name__ == '__main__':
    pytest.main([__file__])
