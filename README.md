# Learning: Math & Technology

My notes and experiments in mathematics and technology, written by an engineer who wants to understand the math underneath the tools.

## Why this exists

Engineering and science run on powerful tools: Fourier transforms, linear algebra, differential equations, probability, optimization, and more recently machine learning. I can use most of them. But I've come to suspect that what holds me back most isn't a missing technique. It's a shaky understanding of the deeper mathematics that makes these tools work, and that explains why they work and when they stop working.

This repository is where I fix that, one topic at a time. Mostly I write for my future self: notes I can read and re-read when I need a reminder. They're public in case they help someone else on a similar path.

## Philosophy

**If you can't explain it simply, you don't understand it.** This is Feynman's test, and it shapes the whole project. Each note tries to explain an idea clearly enough that an intelligent reader without the background could follow it. When I can't write that explanation, I've found a gap in my understanding.

Some related principles:

- **Keep it simple.** Prefer the simplest explanation, example, or code that shows the idea (KISS, Occam's razor). Add complexity only when it is needed.
- **Intuition first, then rigor.** Start with motivation and a concrete example. Then give precise definitions and a proof or proof sketch. Intuition without rigor is fragile, and rigor without intuition is hard to remember. I want both.
- **Bridge pure and applied.** Follow each idea from the abstract math, through the engineering tool built on it, to working code. I want to see the whole chain, from theorem to numbers on a screen.
- **Delve deeper when it pays off.** I have an applied focus, but I'm happy to go into pure math (abstract algebra, analysis, and so on) when it makes the applied picture clearer.

## Structure

```
topics/      Polished notes, one folder per topic (e.g. topics/fourier/)
             Each folder holds Markdown notes and any Python that goes with them
scratch/     Rough explorations, questions, and "what if" experiments
             Anything that turns out well gets cleaned up and moved to topics/
resources/   Books, papers, courses, and links worth returning to
```

## Conventions

- Notes are Markdown with LaTeX math: `$...$` inline, `$$...$$` for display. Both render on GitHub and in VS Code.
- Code is Python, usually with NumPy, SciPy, and Matplotlib. Its job is to make an idea concrete or check it numerically, not to be production software.

## Topics

Areas I expect to cover include applied and computational math (linear algebra, signals and Fourier analysis, probability, numerical methods), the pure math behind them, and eventually AI/ML.
