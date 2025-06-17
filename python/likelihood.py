import matplotlib.pyplot as plt
from math import pi
import numpy as np
from numpy import sqrt
from numpy import exp

# figure 1
# 1d plot
# sigma = 1
# mu = 5
# x = np.linspace(0, 10, 100)
# f = (1/(sigma*sqrt(2*pi)))*exp(-0.5*((x-mu)/sigma)**2)
# plt.plot(x, f, label=r'$\mu=5,\sigma=1$')
# plt.title(r'$f(x;\mu=5, \sigma=1)$')
# plt.legend()
# plt.show()

# Figure 2
# 2d plot
# x_obs = 5
# mu = np.linspace(3, 8, 100)
# sigma = np.linspace(0.1, 2.0, 100)
# MU, SIGMA = np.meshgrid(mu, sigma)
# L = (1 / (SIGMA * sqrt(2 * np.pi))) * exp(-0.5 * ((x_obs - MU) / SIGMA)**2)
# fig = plt.figure(figsize=(10, 6))
# ax = fig.add_subplot(111, projection='3d')
# surf = ax.plot_surface(MU, SIGMA, L, cmap='viridis')
# ax.set_xlabel(r'$\mu$')
# ax.set_ylabel(r'$\sigma$')
# plt.title(r'$L(\mu, \sigma; x=5)$')
# plt.show()

# figure 3
# vertical like likelihood
# sigma = 0.2
# mu = 5.5
# x = np.linspace(0, 10, 1000)
# f1 = (1/(sigma*sqrt(2*pi)))*exp(-0.5*((x-mu)/sigma)**2)
# sigma = 1
# f2 = (1/(sigma*sqrt(2*pi)))*exp(-0.5*((x-mu)/sigma)**2)
# sigma = 2
# f3 = (1/(sigma*sqrt(2*pi)))*exp(-0.5*((x-mu)/sigma)**2)
# plt.axvline(x=5, color='red', linestyle='--')
# plt.plot(x, f1, label=r'$\mu=5.5,\sigma=0.2$')
# plt.plot(x, f2, label=r'$\mu=5.5,\sigma=1$')
# plt.plot(x, f3, label=r'$\mu=5.5,\sigma=2$')
# plt.title('Likelihood function cross sections')
# plt.xlabel("x")
# plt.legend()
# plt.show()

# figure 4
x_1 = 10
x_2 = 10.5
x_3 = 9

mu = np.linspace(8, 12, 100)
sigma = np.linspace(0.1, 2.0, 100)
MU, SIGMA = np.meshgrid(mu, sigma)
pdf1 = (1 / (SIGMA * sqrt(2 * np.pi))) * exp(-0.5 * ((x_1 - MU) / SIGMA)**2)
pdf2 = (1 / (SIGMA * sqrt(2 * np.pi))) * exp(-0.5 * ((x_2 - MU) / SIGMA)**2)
pdf3 = (1 / (SIGMA * sqrt(2 * np.pi))) * exp(-0.5 * ((x_3 - MU) / SIGMA)**2)
L = pdf1*pdf2*pdf3

# MLE estimates
mu_hat = (10 + 10.5 + 9) / 3
sigma_hat = np.sqrt(((10 - mu_hat)**2 + (10.5 - mu_hat)**2 + (9 - mu_hat)**2) / 3)
L_hat = (1 / (sigma_hat * np.sqrt(2 * np.pi)))**3 * np.exp(-0.5 * ((x_1 - mu_hat)**2 + (x_2 - mu_hat)**2 + (x_3 - mu_hat)**2) / sigma_hat**2)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(MU, SIGMA, L, cmap='viridis')
ax.scatter(mu_hat, sigma_hat, L_hat, color='red', s=50)
ax.set_xlabel(r'$\mu$')
ax.set_ylabel(r'$\sigma$')
plt.title(r'$L(\mu, \sigma; x_1=10,x_2=10.5,x_3=9)$')
plt.show()

print(mu_hat)
print(sigma_hat)

# figure 5
x = np.linspace(7, 13, 1000)
f = (1/(sigma_hat*sqrt(2*pi)))*exp(-0.5*((x-mu_hat)/sigma_hat)**2)
plt.axvline(x=9, color='red', linestyle='--')
plt.axvline(x=10, color='red', linestyle='--')
plt.axvline(x=10.5, color='red', linestyle='--')
plt.plot(x, f, label=r'$\mu=9.83,\sigma=0.623$')
plt.title('Maximum likelihood estimate')
plt.xlabel("x")
plt.legend()
plt.show()
