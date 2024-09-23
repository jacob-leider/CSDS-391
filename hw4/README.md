# CSDS 391 (Intro to AI), Homework 4

##### Exercise 3. Repeated state checking for DFS. 
Add repeated state checking to your depth-first search 10P. algorithm. Do this before the working on the next exercise, so that we can compare different search algorithms
more directly.

---

##### Exercise 4: Effective branching factor. 
Write a function to calculate the effective branching factor as used in the table figure 3.26 of the textbook and described in section 3.6.1. The function should take the length of the solution, i.e. the depth d, and find a value b∗ that satisfies the expression for the total number of nodes generated (assuming this effective branching factor)

$$
N + 1 = 1 + b + (b^*)^2 + ... + (b^{*})^d
$$

Note that is not possible to solve this in closed form, so you will have to write an iterative algorithm. Show that your algorithm correctly estimates b∗ by applying it to trees with uniform branching and where the total number of nodes can be calucated analytically.

---

Note that the branching expression can be simplified since the RHS is a geometric series

$$
N + 1 = \sum_{k = 0}^d (b^*)^k = \frac{1 - (b^*)^d}{1 - b^*}.
$$

As we're solving for $b^*$ can be simplified to a degree-$d$ polynomial in $b*$:




---


##### Exercise 5. Comparison of search costs.
You have now implemented four different search algorithms for 15P. solving the 8-puzzle: DFS, BFS, and A* using either the h1 or h2 heuristic. Contrast the nodes generated, the length of solutions, and effective branching factor by generating a table similar to that in figure 3.26. Interpret your table and explain the differences among the different search algorithms.

