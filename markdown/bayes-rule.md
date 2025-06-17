<!-- trick pandoc to not wrapping date in a paragraph tag -->
<em>5/14/25</em>
<h3>Notes on Bayes' rule</h3>

<div style="text-align: center;">
<img src="resources/venn-diagram.svg" width="35%">
</div>

Consider a rectangular dartboard with two circles $A$ and $B$ drawn on it. A monkey is throwing darts at the board, and they fall randomly within it. The probability that the dart falls within the circle labeled $A$ is its area divided by the area of the rectangle, $20/100=0.2$. Now imagine you're facing the other way and the money throws the dart. The bartender tells you it landed in $B$. What is the probability it also landed in $A$ (i.e., in the purple intersection)? It's hopefully intuitive this is the area of the purple section divided by the red section, $4/12=0.33$.

Bayes' rule formalizes this:
$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}\tag{1}
$$

Where $P(A)$ is the probability of event $A$ occurring and $P(A|B)$ is the probability of $A$ occurring given that $B$ occurred. Plugging in the probabilities from the dartboard example, we get the result we expect:
$$
P(A|B)=\frac{(4/20)\times (20/100)}{(12/100)}=4/12=0.33\tag{2}
$$

One way to derive Bayes rule is by starting with the definition of joint probability:
$$
P(A\cap B)=P(A|B)P(B)=P(B|A)P(A)\tag{3}
$$

If you aren't convinced of this fact, consider the dartboard again. You can think of $P(A|B)$ as what % of the red circle is covered by the purple section. Or, in other words, the ratio of the area of the purple section to that of the red section. If we then multiply that by the area of the red section, we're left with the area of the purple section. You can use the same logic to convince yourself of the third term in (3). Finding Bayes' rule is as simple as dividing (3) by $P(B)$.

Let's take a step back, and think more about (1). $P(A|B)$ is a probability and therefore bounded between 0 and 1. How does this fraction ensure this is the case? It's clear that it won't be negative as the three components are all positive. But if $P(B)\to 0$, why wouldn't this fraction grow to infinity? The reason is that $P(B|A)P(A)=P(A\cap B)$ which is strictly less than or equal to $P(B)$. 

In (1), $P(A)$ is called the prior and $P(A|B)$ the posterior since $P(A)$ was our belief about the probability of event $A$ occurring before observing the event $B$, and $P(A|B)$ is our belief about its probability after (prior to) observing $B$.

#### Resources
- [An Introduction to Bayesian Thinking](https://statswithr.github.io/book/): Free online textbook from a Coursera course. Good for someone who has taken an undergraduate stats course 




