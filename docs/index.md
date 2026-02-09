# A Practical Introduction to the Theory of Mathematical Optimization

This site offers a hands-on introduction to the basics of mathematical optimization, guiding you through practical examples in **constraint programming** and **integer programming**.
In constraint programming, we provide just a brief introduction, while in integer programming we dive into more advanced topics, including *constraint generation*, *Benders decomposition*, *column generation*, and *branch-and-cut* (with custom cuts).

All examples are implemented in Python.
The source codes are available at [https://github.com/hmarko89/mathoptintro](https://github.com/hmarko89/mathoptintro/tree/master/src/).

For constraint programming, we use the **Google OR-Tools CP-SAT**, and for integer programming, we use the **Google OR-Tools MathOpt**.
These can be easily installed using the following command:

```
python -m pip install ortools
```

!!! tip "Why python?"
    Python is easy to learn and quick to experiment with, which makes it ideal for teaching and prototyping optimization models.
    At the same time, the heavy computational work is handled by highly optimized solvers written in C/C++, so using Python does not necessarily mean sacrificing performance.
    This allows students to focus on modeling ideas and algorithms rather than low-level implementation details.

!!! tip "Why Google OR-Tools CP-SAT Solver?"
    OR-Tools CP-SAT is one of the leading constraint programming solvers.
    Over the past two years, OR-Tools CP-SAT has won in all categories of <a href="https://www.minizinc.org/challenge/" target="_blank">The MiniZinc Challenge</a>, an annual competition where CP solvers are tested on a wide variety of benchmark problems.

!!! tip "Why Google OR-Tools MathOpt?"
    First of all, if we already use OR-Tools for constraint programming, MathOpt is a natural choice for mathematical programming as well.
    Beyond that, MathOpt is an excellent tool in its own right.

    MathOpt is not a standalone solver; its key idea is the clean separation between modeling and solving.
    At the same time, the interface between the two enables advanced algorithmic features.
    The underlying solver can be easily switched (e.g., SCIP, HiGHS, Gurobi (license required)), and it is possible to implement methods such as column generation or branch-and-cut in a solver-independent way.

    As an alternative, the <a href="https://www.python-mip.com/" target="_blank">`Python-MIP`</a> package can also be used.
    It serves a similar purpose, but supports fewer solvers (CBC and Gurobi), offers fewer callback mechanisms, and is developed less actively.
    