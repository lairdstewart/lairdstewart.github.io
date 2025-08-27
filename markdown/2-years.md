<!-- trick pandoc to not wrapping date in a paragraph tag -->
<em>8/27/25</em>
<h3>Reflections on Two Years Of Software Engineering</h3>

This advice is general, but probably biased by my background with legacy Java applications.

First, work through MIT's "The Missing Semester of Your CS Education" (https://missing.csail.mit.edu)

Useful concepts
- Chesterton's Fence: A hiker comes across a small wooden fence on a beautiful hillside which anyone could step over. He removes it to restore the place's beauty; it wouldn't stop trespassers anyway. Once he has left, over the next months the cows from the neighboring farm eat all its grass and trample it into a muddy slope. When building software, if you encounter something that seems poorly designed, figure out why it was designed that way before refactoring or removing it.
- Pareto Principle (power law): Most real-world relationships are non-linear. E.g., 80% of revenue comes from 20% of customers.

One example of the Pareto Principle is methods which speed up typing:
1. Touch typing
2. Vim key bindings
3. Dvoark layout
4. Ergonomic keyboard
Touch typing will get you 80% of the way to a "pro" typist while Vim keybindings will get you another 15%. Changing keyboard layouts could help a little beyond that. Although touch typing provides 5x more value than Vim keybindings, it's probably about equally as difficult to learn. My suggestion: if you can't already touch type, learn now. Taking "The Missing Semester", reading books about software development, and networking are all better uses of your time than Vim in your first two years.

Minimize configuration. "Every line of configuration is a liability" - ThePrimagen. It's tempting to spend a lot of time configuring your IDE, terminal emulator, and shell. First, remember Chesterton's Fence -- the creators of dev tools designed their tool's features and configuration intentionally (often for their own use!). Another drawback is that you will inevitably need to switch computers, help colleagues, or ssh into a server. These are all more difficult if you can't use default configurations. My suggestion: when starting with a new tool, use its vanilla configuration for the first month (or more). Learn its core features before configuring settings or installing plugins.

Learn the command line versions of tools
1. They are more feature-rich
2. They can be scripted
3. Amortize costs of learning the CLI (terminal emulator, shell) and supporting tools (e.g., tmux, man) across multiple applications.

Try the simple/open source tool first. More often than not it has all the functionality you'll need and is easier to learn. If you discover a functionality it doesn't have, you'll be more prepared to choose a paid offering. For example, VisualVM has suited all my Java profiling needs so far.

I read a few books on software engineering. It was a good use of my time. Ranked (power law applies here):
1. A Philosophy of Software Design -- John Ousterhout
2. Code that Fits in Your Head -- Mark Seemann
3. Working Effectively with Legacy Code -- Michael Feathers
4. Design Patterns -- Gamma, Helm, Johnson, Vlissides
5. Refactoring for Software Design Smells -- Suryanarayana, Samarthyam, Sharma
6. Clean Code -- Robert Martin
