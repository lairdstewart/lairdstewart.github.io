*[Laird Stewart](index.html)*\
*1/5/25*

### Beware of Pithy Rules About Software

The root cause of a lot of bad code is the overuse of common rules (e.g., DRY,
YAGNI, "keep methods under X lines"). These are well-intentioned and distill
years of programming expertise. However, even in a world where they're right 90%
of the time, the 10% of times they're wrong translates to technical debt which
compounds quickly. This isn't to say their creators are at fault; These rules
are often introduced with disclaimers about overuse. The problem is that these
catchy sayings don't have room for disclaimers. After learning a new rule, new
developers may only remember the acronym and not any of its nuances. Senior
developers aren't innocent either; During code review, it's easier to cite a
rule than explain the underlying issue with the code. Teachers don't want to
overwhelm students, so they may give a blanket statement like "don't use static
methods". There is a direct relationship between the length of a piece of advice
and its value. Longer answers can provide context, edge cases, and describe more
sophisticated concepts. It shouldn't be a surprise that short, general
statements can lead us astray.

> "Methods should be shorter than X lines"

The professor of my software design course at Georgia Tech suggested
methods should be under five lines, and *Clean Code* claims *"The first rule of
functions is that they should be small. The second rule of functions is that
they should be smaller than that."* In my mind, this rule is just a heuristic to
remind us that methods should generally only have a single "concept". I argue
that because the former is easier to remember it gets used (and abused) more
frequently. See [It's probably time to stop recommending Clean
Code](https://qntm.org/clean) for an example of how this can go too far. 

> "Don't repeat yourself"

In my first internship, I inherited a thousand-line R script with code literally
copy and pasted half a dozen times with different hard-coded parameters. DRY is
a powerful concept when you first learn it, and I've met a number of data
scientists who could have learned it sooner. However, entry level software
engineers understand copy and pasting code is a red flag. However, it can cause
more harm than good in the form of premature optimization and over-abstraction. 

> "Comments are a failure to express yourself through code"

Early on at my first job, I came across this saying in *Clean Code*. It seemed
reasonable, and my team already used comments sparingly, so I accepted it at face
value. Over my first year, I wrote nearly no comments. I went so far as to leave
PR comments to explain confusing bits because I internalized that putting it in
the code was a failure. I've since grown a much more favorable outlook on
comments. The ultimate irony is that, upon returning to the chapter on comments
in *Clean Code*, I agree almost entirely with it. But because I only remembered
this one saying, my outlook on the topic was quite warped.
