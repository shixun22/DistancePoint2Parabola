# DistancePoint2Parabola
On a 2D Cartesian plane, compute the distace of point (x1, y1) to the parabola: 

$y = eta * (x - a)^2 + b$

dist = min{r^2 = (y - y1)^2 + (x - x1)^2} for (x, y) on parabola 
equivalent to minimizing dr^2/dx / 2 = 2 * eta^2 * (x - a)^3 + 2 * eta * (b - y1) * (x - a) + x - x1 (a cubic polynomial)
