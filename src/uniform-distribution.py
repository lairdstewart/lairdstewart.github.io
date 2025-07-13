import matplotlib.pyplot as plt
import numpy as np

# Create data points for uniform distribution
x = np.linspace(0, 10, 100)
y = np.ones_like(x) * 0.1  # Height is 1/10 for uniform distribution over [0,10]

plt.figure()
plt.plot(x, y, "b-")
plt.fill_between(x, y, alpha=0.2)
plt.grid(True)
plt.xlabel("$x$")
plt.ylabel("Probability Density")
plt.ylim(0, 1.05)
plt.title("Uniform Prior on $x_t$")
plt.savefig("uniform-prior.png")
