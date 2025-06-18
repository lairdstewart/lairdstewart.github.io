<em>6/17/25</em>
<h3>Introduction to Particle Filters</h1>

#### Definition and Vocabulary
> A particle filter is a numerical algorithm to estimate the state of an object given a sequence of measurements about it.

"Numerical" means that particle filters provide an approximate solution using computation. Think of the trapezoid rule for evaluating an integral. This is opposed to an "analytical" solution which provides an exact answer through the manipulation of mathematical formulae. Think of applying rules from calculus class to solve the integral directly. "Estimating state" here means finding a probability distribution on the object's state space. One example of object and state space is a pedestrian (object) and their position/velocity (state space). Another could be a chemical reactor, and it's state space the temperature and concentration of reactants. Next, "measurements" are observations of (or somehow related to) the object's state. For example, the reactor may have a temperature probe inside it. Or, a self-driving car may have a camera which, using computer vision, could place a bounding box around a pedestrian. Notice that the thermometer measures one dimension of the reactors state space (temperature) directly, while the bounding-box does not measure the pedestrian's position or velocity directly—it's impossible to distinguish a short pedestrian nearby from a tall one farther away. "Filter" implies that the algorithm finds an estimate of the objects state at the current time. This is contrasted with "smoothing" which estimates the entire history of its state. Finally, I've mentioned that the output of a particle filter is a probability distribution. In particular, it is a probability density function constructed of a set of "particles". Each particle is a point in the object's state space (e.g., `{x-position, y-position, x-velocity, y-velocity}`) with a corresponding weight. You can think of a particle as a nugget of probability of the object's state. If you're familiar with PDFs and surprised I've suggested using a finite set of things to "construct" a continuous function, hold onto that thought for now.

#### The Kalman Filter 
To motivate particle filters, I'll start by introducing and discussing the limitations of a simpler, analytic solution to this problem known as a Kalman filter. Imagine you're Tom tracking an object (Jerry) who has just entered a hole in the wall and is running towards cheese on the other side. The wall's interior is cluttered, so Jerry's speed will change. As he runs, Tom hears an occasional scratching sound. But the wall is thick and echoey, so these sounds don't come from Jerry's exact location. Given where Jerry entered the wall and the sequence of sounds, Tom wants to estimate Jerry's position.

Tom knows how the wall tends to echo. Given $r_t$, Jerry's position at time $t$, he knows where he is likely to hear a sound: $y_t=g(x;r_t)$ ($a(x;b)$ means $a$ is a function of x "parameterized" by $b$, i.e., $b$ is a constant which appears in $a$'s equation). $y$ typically denotes a measurement, in this case a sound. To be clear, Tom doesn't know $r_t$, he only knows where he *might* hear a sound *if* he knew where Jerry was. $g$ is a 1D Gaussian centered at Jerry's true location with a standard deviation of 5 inches:
$$
\begin{aligned}
&\mathcal{N}(x; \mu, \sigma)=\frac{1}{\sigma\sqrt{2\pi}}\exp(-\frac{1}{2}(\frac{x-\mu}{\sigma})^2)\\
&y_t=g(x; x_t, 5)=\frac{1}{5\sqrt{2\pi}}\exp(-\frac{1}{2}(\frac{x-x_t}{5})^2)\\
\end{aligned}
$$

Tom also knows Jerry typically runs 10 inches per second and that the obstacles vary his speed with $\mathcal{N}(\mu=0, \sigma=1)$. This implies the obstacles are equally likely to speed up or slow down Jerry. Jerry's overall speed is $\mathcal{N}(\mu=10, \sigma=1)$ in/s.

To summarize, we know:
- How fast Jerry typically runs $\mathcal{N}(\mu=3, \sigma=1)$
- How the wall tends to echo: $\mathcal{N}(\mu=x_t,\sigma=0.5)$
- Jerry's initial position and time: $\mathcal{N}(\mu=0,\sigma=0.1)$


<details>
<summary> Proof that the product of two normal distributions is normal </summary>

hello world
$$
y=mx+b
$$
</details>

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

