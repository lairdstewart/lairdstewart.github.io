## On Software Design

This is a living document. I expect to add more ideas and for my philosophy to change over time.

"You know you are working on clean code when each routine you read turns out to be pretty much what you expected" - Ward Cunningham  
"Dealing with complexity is the most important challenge in software design" - John Ousterhout

Favor
- Composition over inheritance
- Simplicity over readability [1]

Strive to
- Make modules deep (Chapter 4 of *A Philosophy of Software Design*)
- Use immutable data and [pure methods](https://en.wikipedia.org/wiki/Pure_function)

Generally
- Methods with side effects should have no return value

I reccomended
- [Amir Hakim: A Minimalist Approach to Software](https://ammar-hakim.org/sj/pn/pn0/pn0-minimalism.html#pn0-a-minimalist-approach-to-software)  
- [John Ousterhout: A Philosophy of Software Design](https://ammar-hakim.org/sj/pn/pn0/pn0-minimalism.html#pn0-a-minimalist-approach-to-software)
--- 
[1] "Readability" is fool's gold. It is often aesthetically and not practically defined. For example, it suggests minimizing the number of arguments to a function. At the extreme, Bob Martin claims "the ideal number of arguments for a function is zero". However, methods without arguments cannot be pure, and I'd prefer a pure method with 3 arguments to an impure method with none.
