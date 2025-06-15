# Introduction to Particle Filters
## Definition and Vocabulary
> A particle filter is a numerical algorithm to estimate the state of an object given a sequence of measurements about it.

First, to introduce some terms. "Numerical" means that it provides an approximate solution using computation. Think of the trapezoid rule for evaluating an integral. This is opposed to an "analytical" solution which provides an exact answer through the manipulation of mathematical formulae. Think of applying rules from calculus class to solve the integral directly. "Estimating state" here means finding a probability distribution on the object's state space. The object's state is unknown, it is the thing we are trying to estimate. One example of object and state space is a pedestrian (object) and their position/velocity (state space). Another could be a chemical reactor, and it's state space the temperature and concentration of reactants. Next, the "measurements" here are things we observe about the state of the object. For example, the reactor may have a temperature probe inside it. Or, a self-driving car may have a camera which, using computer vision, could place a bounding box around a pedestrian. Notice that the thermometer measures one dimension of the reactors state space (temperature) directly, while the bounding-box does not measure the pedestrian's position or velocity directly -- it would not be possible to tell if this was a very tall pedestrian standing far away or a short one nearby. Both of these are types of measurements a particle filter can ingest. "Filter" implies that the algorithm finds an estimate of the objects state at the current time. This is contrasted with "smoothing" which seeks to estimate the entire history of its state. Finally, I've mentioned that the output of a particle filter is a probability distribution. In particular, it is a probability density function constructed of a set of "particles". Each particle is a point in the object's state space (e.g., {x-position, y-position, x-velocity, y-velocity}) with a corresponding weight. You can think of a particle as a nugget of probability of the object's state. If you're familiar with PDFs and surprised I've suggested using a finite set of things to "construct" a continuous function, hold onto that thought for now.

## The Kalman Filter 
To motivate particle filters, I'll start by introducing and discussing the limitations of a simpler, analytic solution to this problem known as a Kalman filter. Consider Tom and Jerry. Jerry just entered a hole in the wall and is running towards cheese on the other side. The interior of the wall is cluttered with obstacles, so through some sections he will run faster and others runs more slowly. As he runs, Tom hears him make an occasional scratching sound. The wall is thick, and a bit echoey, so these sounds may not come from Jerry's exact location. 

Jerry is inside a wall and running back and forth. Tom is outside the wall, and trying to locate Jerry based on the occasional scratching sounds he hears. However, the wall is a bit echo-y so the sounds Tom hears may not be exactly where Jerry is. Given these sounds he needs to estimate Jerry's position.

Tom knows how the wall tends to echo. In other words, given Jerry's position $x_t$, he knows where he is likely to hear a sound: $y_t=g(x;x_t)$ (my notation here means that $g$ is a function of a single variable, x, parameterized by $x_t$) To be clear, Tom doesn't know $x_t$, he only knows where he *might* hear a sound *if* he knew where Jerry was. $g$ is a 1D Gaussian centered at Jerry's true location with a standard deviation of 0.5:
$$
\begin{aligned}
&\mathcal{N}(x; \mu, \sigma)=\frac{1}{\sigma\sqrt{2\pi}}\exp(-\frac{1}{2}(\frac{x-\mu}{\sigma})^2)\\
&y_t=g(x; x_t, 0.5)=\frac{1}{0.5\sqrt{2\pi}}\exp(-\frac{1}{2}(\frac{x-x_t}{0.5})^2)\\
\end{aligned}
$$


To-do: need a simpler scenario where Jerry enters the wall in a hole on the left and moves at a constant speed to the right (with noise). e.g., Tom knows how fast he runs, but not what sort of obstacles is inside the wall, so he could go faster or slower. This is necessary for conjugacy and makes the initial prior easier to describe (just say it is the hole). 

Now, Tom hears a sound ($y_1$) at $x=8$. We have a probability distribution of sound-locations given an (unknown) true position in addition to a sample sound. How can we estimate Jerry's position with this information? The answer is by using a maximum likelihood estimate (MLE). This, at a high level, takes $g$ and re-imagines it as a function of $x_t$ parameterized by $x$: $g'(x_t; x, 0.5)$. We have a value for x (8) which we can plug in here. The domain of $g'$ is likelihoods, and we choose the value of $x_t$ which maximizes $g'$. In this case it is trivial -- it is also 8.




How can we construct a probability distribution on Jerry's state given this? We have a probability distribution of sound-locations given 








Fortunately for Tom, he knows the following things. First, he knows the probabilistic patterns of Jerry's movement. Given Jerry's position at time $t$, $x_t$, he has a probability distribution of Jerry's position at time $t+1$: $x_{t+1}=f(x;x_t)$.
$$
f(x;x_t)=
$$

Here's our first problem, we don't have $x_t$ -- in fact that's what we are trying to find. Fortunately we don't need to know it, we only need a probability distribution of where we thought Jerry was before hearing the sound. This may not sound fortunate, since we knew nothing about his location before the sound! But that is ok, because we can just shrug and give an equal probability to every position. This is called a uniform prior. Uniform because the probability everywhere is the same. A "prior" is just what we call this distribution which represents our knowledge before receiving any data. Assuming the wall is 10 meters long, our uniform prior will look like this:

<img src="uniform-prior.png" alt="Alt text" width="500"/>

Beyond these distributions, Tom has been listening and kept track of the time and location of each sound he has heard. We write this as $y_1, y_2, ... y_t = y_{1:t}$. He wants to guess Jerry's position at time $t$. This is called the filtering problem.

Now, assume we hear the noise at $x=8$. We can use the continuous form of Bayes' rule
$$
\pi^*(p \mid x)=\frac{P(x \mid p) \pi(p)}{\int_0^1 P(x \mid p) \pi(p) d p}
$$

$$
P(x_t=x|\textrm{noise at x=8})=\frac{P(\textrm{noise at x=8}|x_t=x)P(x_t=x)}{P(\textrm{noise at x=8})}
$$



P(noise at x=8) is zero ... how to go from here? 

To-do: use the Gaussian example first to explain how this can be solved analytically, then motivate particle filter by saying the wall is only 10 ft long, and beta distribution isn't quite right.


Question
- what is $f$ called? This suggests that $f$ must be a PDF. Is that correct? Must $g$ be a PDF too? (think so)




update step
- motion model
- prior
- Likelihood
- Resampling

