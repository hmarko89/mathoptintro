# A Practical Introduction to the Theory of Mathematical Optimization

This site offers a hands-on introduction to the basics of mathematical optimization, guiding you through practical examples in **constraint programming** and **integer programming**.
In constraint programming, we provide just a brief introduction, while in integer programming we dive into more advanced topics, including *Benders decomposition*, *column generation*, and *branch-and-cut* (with custom cuts).

All examples are implemented in Python.
For constraint programming, we use the *CP-SAT Solver* from **Google OR-Tools**, and for integer programming, we use the *MathOpt* package from Google OR-Tools.
These can be easily installed using the following command:

```
python -m pip install ortools
```

## Optimization, mathematical optimization

Roughly speaking, optimization is about finding the best solution that satisfies certain requirements.

Formally, if $\mathcal{S}$ is the *set of feasible solutions*, where each solution $S$ has a *cost* $c(S)$, then minimazition can be expressed as

$$
\operatorname{minimize} \{ c(S) : S \in \mathcal{S} \}
$$

For example, in the *traveling salesman problem* there is a directed graph $D=(V,A)$ with a cost function $c: A\to \mathbb{R}$ on the arcs, and the minimum cost Hamiltonian cycle is sought.
That is, the set of feasible solutions is the set of the Hamiltonian cycles of $D$: $\mathcal{S} = \{ S \subseteq A : \delta^+_S(u) = \delta^-_S(u) = 1\text{ for all } u\in V \}$, and $c(S) = \sum_{a\in S} c(a)$ for each $S \subseteq A$.

In **mathematical optimization**, the set of feasible solutions is decribed using *variables* and *constraints*.
In constraing programming, constraints are typically logical conditions, while in integer programming, constraints are expressed as linear inequalities.

### Constraint programming



### Integer programming

