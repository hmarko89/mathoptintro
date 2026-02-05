---
tags:
  - scheduling
---

# Machine Scheduling - A brief introduction

A set $\mathcal{J}$ of *jobs* must be processed on a set $\mathcal{M}$ of *machines* such that each machine can process at most one job at a time, and each job can be processed on at most one machine at a time.

Graham et al. (1979) introduced the 3-field problem classification $\alpha | \beta | \gamma$ for machine scheduling problems, where 
the fields refer to the machine environment, the job characteristics, and the objective funtion, respectively.
For example, $1|r_j|L_{\max}$ denotes the single machine problem, where each job has a release date, and the goal is to minimize the maximum lateness.

!!! quote "Graham et al. (1979)"
    Graham, R. L., Lawler, E. L., Lenstra, J. K., & Kan, A. R. (1979).
    *Optimization and approximation in deterministic sequencing and scheduling: a survey*.
    In Annals of discrete mathematics (Vol. 5, pp. 287-326). Elsevier.

!!! tip "The Scheduling Zoo"
    [The Scheduling Zoo](https://schedulingzoo.lip6.fr/) is an excellent website where you can look up the complexity of machine scheduling problems.

## Machine environment ($\alpha$)

$\alpha = 1$ refers to the single machine case.

$\alpha \in \{ \operatorname{P}, \operatorname{R}, \operatorname{Q} \}$ refers to *parallel machines*, where each job must be assigned to and processed on exactly one machine.
The processing time of job $j$ on machine $i$ is $p_{ij}$.
In case of *identical parallel machines*, $\alpha = \operatorname{P}$, the processing time of a job is the same for all machines, that is, $p_{ij} = p_j$ for all $i$.
In case of *uniform parallel machines* (or *related machines*), $\alpha = \operatorname{Q}$, each machine $i$ has a speed factor $q_i$, and the processing time of a job $j$ on a machine $i$ is $p_{ij} = q_ip_j$.
In case of *unrelated parallel machines*, $\alpha = \operatorname{R}$, there are no such relationship between the processing times.

$\alpha \in \{ \operatorname{O}, \operatorname{F}, \operatorname{J} \}$ refers to *shop problems*, where each job $j$ consists of a set $(O_{1j},\ldots,O_{mj})$ of operations, such that the operation $O_{ij}$ must be processed on machine $i$ with processing time $p_{ij}$.
In case of *open shop*, $\alpha=\operatorname{O}$, the operations can be scheduled in any order.
In case of *flow shop*, $\alpha=\operatorname{F}$, the operations must be scheduled in a given order.
In case of *job shop*, $\alpha=\operatorname{J}$, the operations must be scheduled in a given order, and this order is the same for all jobs.

In case of multiple machines, if the number of the machines, $m$, is fixed, it is indicated in the environment.
For example, $P2$, $F3$, $Jm$, etc.

Environment                 | $\alpha$ | Description
----------------------------|:--------:|------------
Single machine              | 1        | Single machine.
Identical parallel machines | P        | Parallel machines. The processing time of a job is the same for all machines.
Uniform parallel machines   | Q        | Parallel machines. The processing time of a job depends on the speed of the machine.
Related machines            | R        | Parallel machines. 
Open shop                   | O        | Shop problem.
Flow shop                   | F        | Shop problem. Operation order is fixed for each job. 
Job shop                    | J        | Shop problem. Operation order is fixed, and the same for all jobs.

## Constraints ($\beta$)

The processing times ($p_{ij}$ or $p_{j}$) are always given, thus their presence is never indicated in the $\beta$-field,
Each job $j$ may have a *due date* $d_j$, by which it should ideally be completed.
Each job $j$ may also be associated with a *weight* priority $w_j$. 
Parameters $d_j$ and $w_j$ are never indicated in the $\beta$-field; if the objective function requires them, we simply assume they are given.

Several constraints can be indicated in the $\beta$-field.
Here, we present a few examples that will be used later.

Jobs may be associated with a release date $r_j$, indicating their earliest possible start time.

Jobs (or operations) may require a preparation time.
In case of *sequence-dependent setup times*, preparation times depend on the predecessor job (or operation), if any.

Constraint                     | $\beta$ | Description
-------------------------------|:-------:|------------
Release times                  | $r_j$   | Earliest start times for jobs.
Sequence-dependent setup times | $sds$   | Changing time between jobs.

## Objective function ($\gamma$)

For a given schedule $S$, let $C^S_j$ denote the *completion time* of job $j$.
Note that, in the non-preemptive case, the assignment of jobs to machines together with their completion times fully describes the schedule.

The *makespan* of the schudule is the maximum completion time of the jobs: $C^S_{\max} = \max_{j \in \mathcal{J}}C^S_j$.
The *lateness* of a job $j$ is $L^S_j = C^S_j - d_j$, while its *tardiness* is $T^S_j = \max\{0,L^S_j\}$.
Let $U^S_j = 1$ if job $j$ is late (i.e., $0 < L^S_j$), and 0 otherwise.

The *flow time* of a job $j$ is $F^S_j = C^S_j - r_j$.

Objective ($\gamma$) | Description
---------------------|------------
$C_{\max}$           | Minimizing the *makespan*, i.e., the maximum completion time.
$\sum C_j$           | Minimizing the *sum of completion times*.
$\sum w_jC_j$        | Minimizing the *weighted sum of completion times*.
$L_{\max}$           | Minimizing the *maximum lateness*.
$\sum T_j$           | Minimizing the *total tardiness*.
$\sum w_jT_j$        | Minimizing the *weighted tardiness*.
$\sum U_j$           | Maximizing the *throughput*, that is, minimizing the *number of late jobs*.
$\sum w_jU_j$        | Maximizing the *weighted throughput*, that is, minimizing the *total weight of late jobs*.
$\sum F_j$           | Minimizing the *maximum flow time*.
