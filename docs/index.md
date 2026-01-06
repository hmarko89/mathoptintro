# A Practical Introduction to the Theory of Mathematical Optimization

This site offers a hands-on introduction to the basics of mathematical optimization, guiding you through practical examples in **constraint programming** and **integer programming**.
In constraint programming, we provide just a brief introduction, while in integer programming we dive into more advanced topics, including *Benders decomposition*, *column generation*, and *branch-and-cut* (with custom cuts).

All examples are implemented in Python.
For constraint programming, we use the *CP-SAT Solver* from **Google OR-Tools**, and for integer programming, we use the *MathOpt* package from Google OR-Tools.
These can be easily installed using the following command:

```
python -m pip install ortools
```

## Optimization

Roughly speaking, optimization is about finding the best possible solution that satisfies certain requirements.

Formally, if $\mathcal{S}$ is the *set of feasible solutions*, where each $S \in \mathcal{S}$ *solution* has a *cost* $c(S)$, then minimization can be expressed as:

$$
\operatorname{minimize} \{ c(S) : S \in \mathcal{S} \}
$$

In many *graph optimization problems*, feasible solutions are certain subsets of edges that satisfy a prescribed combinatorial structure.
Let $G=(V,E)$ be a graph with a cost function $c: E\to \mathbb{R}$ defined on the edges.
For any subset $S \subseteq E$ of edges, let $c(S) := \sum_{e\in S}c(e)$.
For example, in the shortest path problem, the goal is to find a minimum-cost path between two designated nodes $s$ and $t$.
In this case, $\mathcal{S}$ is the set of all $s-t$ paths in $G$.
In the *traveling salesman problem*, $\mathcal{S}$ is the set of all Hamiltonian cycles of the graph.

In **mathematical optimization**, the set of feasible solutions is decribed using *variables* and *constraints*.
In constraing programming, constraints are typically logical conditions, while in integer programming, constraints are expressed as linear inequalities.

### Constraint programming



### Integer programming


