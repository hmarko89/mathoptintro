# Optimization

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

## Constraint programming



## Integer programming