import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad

def gamma(z):
    integrand = lambda t: t**(z - 1) * math.exp(-t)
    result, _ = quad(integrand, 0, math.inf)
    return result

def B(a, b):
    return gamma(a) * gamma(b) / gamma(a + b)

def beta_pdf(x, a, b):
    x = np.asarray(x)
    pdf = np.zeros_like(x, dtype=float)
    valid = (x >= 0) & (x <= 1)
    norm = B(a, b)
    pdf[valid] = (x[valid]**(a - 1)) * ((1 - x[valid])**(b - 1)) / norm
    return pdf


x = np.linspace(0, 1, 100)
y = beta_pdf(x, 1, 1)

plt.figure()
plt.plot(x, y, 'b-')
plt.fill_between(x, y, alpha=0.2)
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('Probability Density')
# plt.ylim(0, 1.05)
plt.title('Beta distribution pdf on $x_t$')
plt.show()
# plt.savefig('uniform-prior.png')
