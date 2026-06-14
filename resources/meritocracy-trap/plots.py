from ipumspy import readers
from scipy.stats import truncnorm
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, lognorm
from scipy.optimize import minimize
from scipy.stats import truncnorm

"""
Load data. Must be downloaded from 
"""

ddi = readers.read_ipums_ddi("cps_00001.xml")
data = readers.read_microdata(ddi)

working_adults = data[
    (data["AGE"] >= 18)
    # employed, at work / has job not at work
    & (data["EMPSTAT"].isin([10, 12]))
    & (data["INCTOT"] > 0)
    # IPUMS missing value code
    & (data["INCTOT"] != 9999999)
][["INCTOT", "ASECWT"]]

incomes = working_adults["INCTOT"].values
weights = working_adults["ASECWT"].values
weights = weights / weights.sum()

"""
Plot income distribution histogram
"""

plt.figure(figsize=(12, 6))
plt.hist(
    incomes,
    bins=100,
    weights=weights,
)

plt.xlabel("Annual Income ($)")
plt.ylabel("Number of People")
plt.title("US Individual Income Distribution")
plt.gca().xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"${x:,.0f}")
)
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"{x/1_000_000:.1f}M")
)
plt.tight_layout()
plt.show()

"""
Plot Quantile Function
"""
sorted_indices = np.argsort(incomes)
sorted_incomes = incomes[sorted_indices]
sorted_weights = weights[sorted_indices]

percentiles = []
percentile_incomes = []
cumsum = 0.0
target = 0.001

for i in range(len(sorted_weights)):
    cumsum += sorted_weights[i]
    while target <= cumsum and target <= 1.0:
        percentiles.append(target)
        percentile_incomes.append(sorted_incomes[i])
        target += 0.001

# percentiles.append(1)
# percentile_incomes.append(sorted_incomes[-1])

plt.figure(figsize=(12, 6))
plt.plot(percentiles[100:-10], percentile_incomes[100:-10])
# plt.axvline(x=0.91, color="red", alpha=0.5)
# plt.axvline(x=0.95, color="red", alpha=0.5)
# plt.axvline(x=0.99, color="red", alpha=0.5)
plt.xlabel("Percentile")
plt.ylabel("Annual Income ($)")
plt.title("US Individual Income Distribution by Percentile")
plt.gca().xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"{x*100:.0f}th")
)
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"${x:,.0f}")
)
plt.tight_layout()
plt.show()

"""
Plot log Quantile Function
"""
plt.figure(figsize=(12, 6))
plt.plot(percentiles[100:-10], np.log(percentile_incomes[100:-10]))
plt.xlabel("Percentile")
plt.ylabel("Log Annual Income ($)")
plt.title("US Individual Income Distribution by Percentile (log scale)")
plt.gca().xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"{x*100:.0f}th")
)
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"${x:,.0f}")
)
plt.tight_layout()
plt.show()
