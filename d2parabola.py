"""    
distace of point (x1, y1) to
parabola: y = eta * (x - a)**2 + b
dist = min{r^2 = (y - y1)**2 + (x - x1)**2} for (x, y) on parabola -> minimizing dr^2/dx / 2 = 2 * eta**2 * (x - a)**3 + 2 * eta * (b - y1) * (x - a) + x - x1 (a cubic polynomial)
"""

import numpy as np

def d2parabola(x1, y1, eta, a, b):
    def dist(x_para):
        """        
        distance of (x1, y1) to point on parabola with x=x_para
        """
        y_para = eta * (x_para - a)**2 + b
        return ((y_para - y1)**2 + (x_para - x1)**2)**0.5

    params = [2 * eta**2, -6 * a * eta**2, 6*a**2 * eta**2 + 2 * eta * (b - y1) + 1, -2 * a**3 * eta**2 - 2 * a * eta * (b - y1) - x1] # coefficients of the cubic polynomial dr^2/dx / 2
    roots = np.roots(params)
    x_para = roots[np.isreal(roots)].real
    dd = dist(x_para).min()
    return dd


