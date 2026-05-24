#import "@preview/touying:0.6.1": *
#import themes.simple: *
#show link: set text(fill: blue)
#show link: underline

#show: simple-theme.with(aspect-ratio: "16-9", header: none)

= 2026: Year of the DevOp
\

== The supercharged developer

- Ask questions about a codebase
- Autocomplete multiple lines at once
- Write a method from scratch. 

== 

- 90% of code written at Anthropic is by Claude
- 4% of commits on GitHub are authored by Claude (0.3% in October)

== 

Claude is *not* proactive

== 

1. Context
2. Verification

== Context

#text(20pt)[
1. Anthropic system prompt
2. Claude.md
3. Claude's "memory" in ~/.claude
4. Your prompt
5. Things Claude looks up itself
  - Source files
  - Documentation
  - CLI tools (e.g., Grep, Maven, GitHub CLI)
  - MCP (e.g., Google search)
6. Agent Skills (aka. slash commands)
7. Current session's conversation history
8. Sub-agent output
]

== Verification

1. Compile/Build script
2. Unit Tests
3. Browser MCP

== Workflow
- GitHub issues
- "Ticket" skill
- Parallel agents via. Git worktrees
- Visual/audio notifications

== Demo

==
#align(center)[
  #image("scaling-laws.png", width: 100%)
]

#align(center)[
  #image("time-horizon.png", width: 100%)
]

#align(center)[
  #image("token-cost.png", width: 100%)
]


// #align(center)[
//   #image("/resources/SimpleBayesNet.png", width: 55%)
// ]
// #link("https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf")[A Fast Learning Algorithm for Deep Belief Nets]
