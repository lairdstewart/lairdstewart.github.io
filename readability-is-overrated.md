*1/25/25*

### Readability is Overrated
"Dealing with complexity is the most important challenge in software design" -
John Ousterhout

When I say a piece of code is readable I typically mean understandable or
grokable. And I typically take others to mean that as well. However, it seems
that some think of readable code like they think of readable prose: that which is
straightforward, simple, and pleasing. Code and prose share many similarities,
but they are not the same. Therefore, we shouldn't expect our preferences for
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
difficulty of the problem the code is solving. The problem may require a
complicated algorithm or advanced data structure with irreducible complexity.
Therefore, I suggest minimizing the difference in complexity between the
underlying problem and the code written to solve it.
