To illustrate the particle filter, its best to start with a 1-dimensional example. Consider the cartoon Tom and Jerry. Imagine Jerry is inside a wall and running back and forth. Tom is trying to locate Jerry but can't see through the wall and only occasionally hears cartoon scratching sounds. Given these sounds he wants to place a trap (and needs to estimate Jerry's position). Fortunately for Tom, he knows the following things. 

Given Jerry's position at time $t$, 

$x_t=f(x_{t-1})$  (pdf). Given the previous state of the target, 
$y_t=g(x;x_t)$ (pdf)

We recieve $y_{1:t}$ and want to estimate $x_t$ this is called the filtering problem.

$L(\mu,\sigma; x)$


$$
x_{t+1}=\frac{}{}
$$


update step

- motion model
- prior
- Likelihood
- Resampling