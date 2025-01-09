# On Software Design
"Dealing with complexity is the most important challenge in software design" -
John Ousterhout

### Beware pithy rules
The root cause of a lot of bad code is the overuse of common rules (e.g., DRY,
YAGNI, "keep methods under X lines"). These are well intentioned and distill
years of programming expertise. However, even in a world where they're right 90%
of the time, the 10% times they are wrong translates to technical debt which
compounds quickly. This isn't to say their creators are at fault; These rules
are often introduced with disclaimers about overuse. The problem is that pithy
sayings don't have room for disclaimers. After learning a new rule, new
developers may only remember the acronym and not any of its nuances. Senior
developers aren't innocent either; During code review, it's easier to cite a
rule than explain the underlying issue with the code. Teachers don't want to
overwhelm students, so they may give a blanket statement like "don't use static
methods". There is a direct relationship between the length of a piece of advice
and its value. Longer answers can provide context, edge cases, and describe more
sophisticated concepts. It shouldn't be a surprise that short, general
statements can lead us astray.

You've likely heard some version of the rule *"methods should be shorter than X
lines"*. The professor of my software design course at Georgia Tech suggested
methods should be under five lines, and *Clean Code* claims *"The first rule of
functions is that they should be small. The second rule of functions is that
they should be smaller than that."* In my mind, this rule is just a heuristic to
remind us that methods should generally only have a single "concept". I argue
that because the former is easier to remember it gets used (and abused) more
frequently. See [It's probably time to stop recommending Clean
Code](https://qntm.org/clean) for an example of how this can go too far. 

Another example is DRY. In my first internship, I inherited a hundred-line R
script with code literally copy and pasted half a dozen times with different
hard-coded parameters. DRY is a powerful concept when you first learn it and
I've met a number of data scientists who could have learned it sooner. However,
entry level software engineers understand copy and pasting code is a red flag.
Therefore it may cause more harm than good in the form of premature optimization
and over-abstraction. 

### Readability is Overrated
When I say a piece of code is readable I typically mean understandable or
grokable. And I typically take others to mean that as well. However, it seems
that some think of readable code like they think of readable prose: that which is
straightforward, simple, and pleasing. Code and prose share many similarities,
but they are not the same. Therefore we shouldn't expect our preferences for
clearly written English to translate to good code. According to this definition,
Example 3-7 from Clean Code is readable.  `includeSetupAndTeardownPages()` is
visually clean, quick to read, and appears straightforward. However, after
reading this you have no idea what it does or how it works. Which fields does it
update? Where does the exception come from? Would it break if the order of the
methods changed?

```java
// from example 3-7 of Clean Code
private PageData pageData;
private boolean isSuite;
private WikiPage testPage;
private StringBuffer newPageContent;
private PageCrawler pageCrawler;

private void includeSetupAndTeardownPages() throws Exception {
    includeSetupPages();
    includePageContent();
    includeTeardownPages();
    updatePageContent();
}
```

Understandability isn't a great metric either because it's relative. Senior devs
can grok code more quickly than junior devs. A developer with vim motions and
keybindings to jump between methods will find deeply nested code easier to
understand. Most important, code's understandability is relative to the
difficulty of the problem the code is solving. The problem may required a
complicated algorithm or advanced data structure with irreducible complexity.
Therefore I suggest minimizing the difference in complexity between the
underlying problem and the code written to solve it.

### Comments are Underrated
Most developers have proper experience and good intentions, but most code isn't
good. Whether it's deadlines, changing requirements, or simply time, code is
almost never

### I recommend
- [A Minimalist Approach to Software (Ammar Hakim)](https://ammar-hakim.org/sj/pn/pn0/pn0-minimalism.html#pn0-a-minimalist-approach-to-software)
- [A Philosophy of Software Design (John Ousterhout)](https://web.stanford.edu/~ouster/cgi-bin/book.php)
---
https://htmx.org/essays/locality-of-behaviour/


