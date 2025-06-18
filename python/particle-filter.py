import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Any
import numpy.typing as npt
from numpy import floating

floats = npt.NDArray[floating[Any]]


def N(mu: float, sigma: float) -> Callable[[floats], floats]:
    def f(x: floats) -> floats:
        return (
            1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) ** 2) / (2 * sigma**2))
        )

    return f


x: floats = np.linspace(0, 10, 100)
y: floats = N(0, 0.1)(x)

fig, ax = plt.subplots()  # type: ignore
ax.plot(x, y, "b-")  # type: ignore
ax.fill_between(x, y, alpha=0.2)  # type: ignore
ax.grid(True)  # type: ignore
ax.set_xlabel("$x$")  # type: ignore
ax.set_ylabel("Probability Density")  # type: ignore
ax.set_ylim(0, 1.05)  # type: ignore
ax.set_title("Uniform Prior on $x_t$")  # type: ignore
plt.show()  # type: ignore
