# Introduction to Constraint Programming

If you have ever solved a *Sudoku* puzzle, you will find it easy to understand the basics of **constraint programming** (*CP*).

??? example "Sudoku – How to solve it on paper?"
    In sudoku, there is a partially filled grid of size $9\times 9$.
    The goal is to write a number from $1,\ldots,9$ in each empty cell, such that each column, each row, and each of the nine $3\times 3$ subgrids that compose the grid contains all numbers from $1,\ldots,9$ exactly once.

    So, how would you solve such a puzzle?
    I bet you grab a pencil (recommended only for printed version!) and write the remaining possible values for each empty cell in small writing.
    For example, if a number, say 4, is definitely placed in a cell, then the number 4 can be removed from the possible values of the cells in the same row, in the same column, and in the same subgrid.
    If a cell ends up with only one possible value, you can write that value boldy.
    Depending on the difficulty of the puzzle, you may eventually reach a point where this tactic is no longer sufficient to continue solving.

    However, you can also try to eliminate impossible values using a bit of logic plus some courage and a dash of luck.
    Pick a cell, write one of the remaining candidate numbers lightly, and see what happens when you apply the previous elimination tactics again.
    If you are lucky, you will quickly find out whether you made a bad choice: some contradiction will appear — for example, a cell ends up with no valid values left according to the rules.
    In that case, you can safely remove the number you just tried from the cell’s possible candidates.
    If you do not get lost in the bookkeeping, this "trial and error" strategy will guarantee the solution to the puzzle.

    This solving strategy sketched for Sudoku is pretty close to the classic way CP solvers tackle problems.

## Constraint Satisfaction Problem

A **constraint satisfaction problem** (*CSP*) is defined as a triplet $(\mathcal{X},\mathcal{D},\mathcal{C})$, where:

- $\mathcal{X}=(\mathbf{x}_1,\ldots,\mathbf{x}_n)$ is a set of **variables**;
- $\mathcal{D}=(D_1,\ldots,D_n)$ is the set of **domains** of the variables; and
- $\mathcal{C}$ is a finite set of **constraints**.

A constraint $(X,R)$ is defined by a set $X = \{ \mathbf{x}_{i_1},\ldots,\mathbf{x}_{i_m} \} \subseteq \mathcal{X}$ of variables and a **relation** $R \subseteq D_{i_1} \times \ldots \times D_{i_m}$ that defines the set of values allowed simultaneously for those variables.
We distinguish three categories of constraints:

- **Extensional constraints** are defined by explicitly listing all allowed combinations of values for the involved variables.
- **Arithmetic constraints** are defined by an arithmetic expression ($<$, $\leq$, $>$, $\geq$, $=$, $\neq$, etc.).
- **Logical constraints** are defined with an explicit logical semantics.

!!! tip "The `alldifferent` constraint"
    The `alldifferent` logical constraint requires that the given variables take pairwise distinct values:

    $$
    \operatorname{alldifferent}(\mathbf{x}_{i_1},\ldots,\mathbf{x}_{i_m}) \longleftrightarrow \left( (\mathbf{x}_{i_1},\ldots,\mathbf{x}_{i_m}), \left\{ (d_{i_1},\ldots,d_{i_m}) \subseteq D_{i_1} \times \ldots \times D_{i_m} : j\neq k \Rightarrow d_{i_j} \neq d_{i_k} \right\} \right)
    $$

    Check the `alldifferent` constraint in the [Global Constraint Catalog](https://sofdem.github.io/gccat/gccat/Calldifferent.html#uid13010).

A **solution** for the CSP is a total assignement $(d_1,\ldots,d_n)$ of values to variables such that:

- the values are selected from the domains, that is, $d_i \in D_i$ holds for $i=1,\ldots,n$; and
- each constraint $((\mathbf{x}_{i_1},\ldots,\mathbf{x}_{i_m}),R)\subseteq \mathcal{C}$ is satisfied, that is, $(d_{i_1},\ldots,d_{i_m}) \in R$.

??? example "Sudoku – Modelling as a CSP"
    Note that this brief introduction is already enough to model Sudoku as a CSP.
    Each cell is associated with a variable, such that empty cell variables have domain $\{1,\ldots,9\}$, while pre-filled cell variables are fixed to their given value.
    For each row, each column, and each subgrid, we impose an `alldifferent` constraint to ensure that all numbers are distinct.

    For details, see [the next page](./sudoku.md).

## Propagators

Each constraint is associated with a **propagator**, which is a process that tries to shrink the domains of the variables involved in that constraint — in other words, it removes values that cannot appear in any solution.

Whenever the domain of a variable changes, the propagators of all constraints containing that variable are triggered, which may in turn trigger more propagator calls, and so on...

It can happen that, at the end of this propagator-avalanche, a variable's domain becomes empty, which proves that the problem has no solution.
Otherwise, we say that all constraints — and therefore the whole problem — are *locally consistent*.

??? example "Sudoku – Propagating"
    The tactic we used in Sudoku to eliminate impossible values from cells is basically the propagators of the `alldifferent` constraints in action.

### Local consistency

A constraint $((\mathbf{x}_{i_1},\ldots,\mathbf{x}_{i_m}),R)$ over $m$ variables is **hyper-arc consistent** if for every variable $\mathbf{x}_{i_k}$ ($1\leq k\leq m$) and for every value $d \in D_{i_k}$ in its domain, there exists a feasible assignment $(d_{i_1},\ldots,d_{i_m}) \in R$ with $d_{i_k} = d$.
In other words, no value in any variable's domain can be removed based on this constraint alone.

!!! note "Node consistency ($m=1$)"
    \[
      \left.\begin{array}{r}
      1 < x_i\\
      x_i \leq 4\\
      x_i \in \{0,1,2,3,4,5\}
      \end{array}\right\}\quad\Rightarrow
      \left.\begin{array}{r}
      1 < x_i\\
      x_i \leq 4\\
      x_i \in \{2,3,4\}
      \end{array}\right\}
    \]

    Clearly, $x_i$ cannot be 0 or 1 because of the first constraint, and it cannot be 5 because of the second constraint.
    After propagation, the variable's domain is reduced, and both constraints are **node-consistent**.

!!! note "Arc consistency ($m=2$)"
    \[
      \left.\begin{array}{r}
      x_i + 2x_j = 9\\
      x_i \in \{0,1,2,3,4,5\}\\
      x_j \in \{0,1,2,3,4,5\}
      \end{array}\right\}\quad\Rightarrow
      \left.\begin{array}{r}
      x_i + 2x_j = 9\\
      x_i \in \{1,3,5\}\\
      x_j \in \{2,3,4\}
      \end{array}\right\}
    \]
    
    Clearly, $x_i$ cannot be even.
    Then the domain of $x_j$ can also be reduced, because for values $0,1,5$ there is no suitable value for $x_i$ that satisfies the constraint.
    After this propagation, the constraint is **arc-consistent**.

!!! note "Local consistency for the `alldifferent` constraint"
    The `alldifferent` constraint can be represented as a bipartite graph: variable nodes correspond to the variables, value nodes correspond to the possible values, and a variable node is connected to a value node if that value is in the variable's domain.

    Each matching that covers all variable nodes corresponds to a feasible assignment, and vice versa.

    Propagation: edges that do not appear in any matching can be removed, reducing the domains of the variables.

## Branch-and-Propagate

If during propagation the domain of any variable becomes empty, it is proven that the problem has no solution.

If, at the end of propagation, every variable's domain contains exactly one value, then that is the solution.

Otherwise, propagation must be embedded into a **tree search** scheme, meaning that the problem has to be split into multiple subproblems (branches).
For example, if a variable $x_i$ has $k$ possible values, say $D_i=\{d_1,\ldots,d_k\}$, we can create $k$ branches, and in the $j$th branch, we require that $x_i = d_j$.

??? example "Sudoku – Branch-and-Propagate"
    When we "guessed" in Sudoku — i.e., checked what would happen if we wrote a chosen number into a cell — we were basically performing a branching.
    
## Optimization

So far, we have not discussed optimization; we were only looking for a feasible solution.
But what if we have an objective function?
This can be handled in several ways, for example by an iterative approach: once a feasible solution is found, in the next iteration we add a constraint requiring the objective function value to be better than in the previous solution.
For example, <a href="https://deepwiki.com/google/or-tools/4.1-cp-sat-constraint-programming-solver" target="_blank">OR-Tools CP-SAT</a> is a hybrid solver as it combines techniques from constraint programming, SAT solving, and mixed-integer programming.
