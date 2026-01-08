---
tags:
  - cp
  - scheduling
---

# Machine Scheduling with Constraint Programming

Machine scheduling is about to schedule the processing of a set $\mathcal{J}$ of *jobs* on a set $\mathcal{M}$ of *machines* such that each machine can process at most one job at a time, and each job can be processed on at most one machine at a time.
For a more detailed introduction, check the page [Machine Scheduling](../../intro/scheduling).

Here, we focus on the **single-machine problem** and solve it using constraint programming. 
We will get familiar with the *interval variables* and the *no-overlap constraints*.

## Problem definition

We consider the problem $1|r_j|\sum w_j C_j$.
That is, each job $j\in\mathcal{J}$ has:

- a **processing time** $p_j$,
- a priority **weight** $w_j$,
- a **release date** $r_j$,

and the goal is to minimize the **weighted sum of completion times**.

## CP formulation

Let simply $\mathcal{J}=\{1,\ldots,n\}$.

### Variables (and constraints)

!!! tip "Interval variables"
    An **interval variable** allows to model an interval of time.

    Acctually, it is both a variable and a constraint.
    It is a constraint, since it ties together multiple variables (start, duration, end, etc.) and enforces their relationships.
    It is a variable, since it can appear in multiple constraints.

    Google OR-Tools provides several types of interval variables, for example:
    `new_interval_var`, `new_fixed_size_interval_var`, `new_optional_interval_var`, and `new_optional_fixed_size_interval_var`.

Let be the interval variable $\mathbf{I}_j = [\mathbf{S}_j,\mathbf{C}_j]$ associated with job $j$.
That is, $\mathbf{S}_j$ and $\mathbf{C}_j$ indicate the start and the completion time, respectively, of the job, where $\mathbf{C}_j = \mathbf{S}_j + p_j$ must hold.

### Constraints

!!! tip "No-overlap constraints"
    A **disjuncive constraint** (or **no-overlap constraint**) ensures that the given intervals do not overlap.

    For example, Google OR-Tools provides: `add_no_overlap` (for one-dimensional intervals) and `add_no_overlap_2d`(for two-dimensional intervals).

    Check the `disjunctive` constraint in the [Global Constraint Catalog](https://sofdem.github.io/gccat/gccat/Cdisjunctive.html#uid19717).    

With such a constraint, we can easily formulate the scheduling constraints:

$$
\operatorname{disjunctive}(\mathbf{I}_1,\ldots,\mathbf{I}_n)
$$

### Objective

The objective is to minimize the weighted sum of completion times:

$$
\operatorname{minimize} \sum_{j\in \mathcal{J}} w_j\mathbf{C}_j
$$

## Implementation

