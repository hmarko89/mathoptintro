# A Practical Introduction to the Theory of Mathematical Optimization

This site offers a hands-on introduction to the basics of mathematical optimization, guiding you through practical examples in **constraint programming** and **integer programming**.
In constraint programming, we provide just a brief introduction, while in integer programming we dive into more advanced topics, including *Benders decomposition*, *column generation*, and *branch-and-cut* (with custom cuts).

All examples are implemented in Python.
For constraint programming, we use the *CP-SAT Solver* from **Google OR-Tools**, and for integer programming, we use the *MathOpt* package from Google OR-Tools.
These can be easily installed using the following command:

```
python -m pip install ortools
```

The source codes are available at [https://github.com/hmarko89/mathoptintro](https://github.com/hmarko89/mathoptintro/tree/master/src/).

!!! tip "Why python?"

!!! tip "Why Google OR-Tools CP-SAT Solver?"
    Google OR-Tools CP-SAT is one of the leading constraint programming solvers.
    Over the past two years, OR-Tools CP-SAT has won in all categories of [The MiniZinc Challenge](https://www.minizinc.org/challenge/), an annual competition where CP solvers are tested on a wide variety of benchmark problems.

!!! tip "Why Google OR-Tools MathOpt?"
    
