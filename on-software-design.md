## On Software Design

This is a living document. I expect to add more ideas and for my philosophy to change over time.

"You know you are working on clean code when each routine you read turns out to be pretty much what you expected" - Ward Cunningham  
"Dealing with complexity is the most important challenge in software design" - John Ousterhout

- Favor composition over inheritance
- Minimize complexity don't maximize readability [1]
- Make modules deep (Chapter 4 of *A Philosophy of Software Design*)
- Strive to use immutable data and [pure methods](https://en.wikipedia.org/wiki/Pure_function)
- Methods with side effects should have no return value

I reccomended
- [Amir Hakim: A Minimalist Approach to Software](https://ammar-hakim.org/sj/pn/pn0/pn0-minimalism.html#pn0-a-minimalist-approach-to-software)  
- [John Ousterhout: A Philosophy of Software Design](https://ammar-hakim.org/sj/pn/pn0/pn0-minimalism.html#pn0-a-minimalist-approach-to-software)
--- 
[1] Over-indexing on readability can turn code to fool's gold. By this I mean code that has many methods with simple names. It looks clean, but only at first glance. For example, methods with fewer arguments are more readable. At the extreme, Bob Martin claims "the ideal number of arguments for a function is zero". In my opinion, the "ideal" method is pure, but methods without arguments must be impure! Simmilarly, splitting a method in two makes their declarations more readable when read one after the other, but it could add complexity via a new field variable and/or an implicit assumption about the order they must be called in. Listing 2-2 of *Clean Code* is an example of fool's gold and [Don't Refactor Like Uncle Bob. Please](https://theaxolot.wordpress.com/2024/05/08/dont-refactor-like-uncle-bob-please/) has a nice way to refactor it.

