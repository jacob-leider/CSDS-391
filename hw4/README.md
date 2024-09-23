# CSDS 391 (Intro to AI), Homework 4

##### Exercise 3. Repeated state checking for DFS. 
Add repeated state checking to your depth-first search 10P. algorithm. Do this before the working on the next exercise, so that we can compare different search algorithms
more directly.

---

##### Exercise 4: Effective branching factor. 
Write a function to calculate the effective branching factor as used in the table figure 3.26 of the textbook and described in section 3.6.1. The function should take the length of the solution, i.e. the depth d, and find a value b∗ that satisfies the expression for the total number of nodes generated (assuming this effective branching factor)

$$
N + 1 = 1 + b + (b^\*)^2 + ... + (b^{\*})^d
$$

Note that is not possible to solve this in closed form, so you will have to write an iterative algorithm. Show that your algorithm correctly estimates b∗ by applying it to trees with uniform branching and where the total number of nodes can be calucated analytically.

---

Note that the branching expression can be simplified since the RHS is a geometric series

$$
N + 1 = \sum_{k = 0}^d (b^\*)^k = \frac{1 - (b^\*)^d}{1 - b^\*}.
$$

As we're solving for $b^\*$ can be simplified to a degree- $d$ polynomial in $b^\*$:

$$
(b^\*)^d - (N + 1)b^\* + N = 0
$$

We use the geometric series formula even though the expression is already a polynomial, since the number of nonzero coefficients in the new expression is constant, while $O(d)$ in the previous expression.

For $N > d, b^\*$ is always the greatest real root (three distinct real roots, one negative, one equal to one and one greater than one). Thus, we can  simply find an upper bound and use it as an initial guess in newtons method. A good upper-bound is N/d, since (if $N > d$ )

$$\sum_{k = 0}^d \left(\frac{N + 1}{d}\right)^k \geq d\left(\frac{N + 1}{d}\right) = N + 1.$$

Another good upper bound is $\sqrt[d]{N + 1}$ (this one is pretty trivial). The latter is better when $N >> d$ and the former is better when $N$ is close to $d.$ 

The implementation of this function can be found in `heuristics.py`.



---


##### Exercise 5. Comparison of search costs.
You have now implemented four different search algorithms for 15P. solving the 8-puzzle: DFS, BFS, and A* using either the h1 or h2 heuristic. Contrast the nodes generated, the length of solutions, and effective branching factor by generating a table similar to that in figure 3.26. Interpret your table and explain the differences among the different search algorithms.


| d | BFS | DFS | A*(h1) | A*(h2) | BFS | DFS | A*(h1) | A*(h2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6  | 89  | 160293 | 14 | 14 | 1.87 | 1.00 | 1.25 | 1.25 |
| 8  | 371 | 122756 | 35 | 24 | 1.91 | DFS | 1.33 | 1.24 |
| 10 | 754 | 167804 | 71 | 30 | 1.79 | DFS | 1.34 | 1.19 |
| 12 | 2685 | 172533 | 121 | 59 | 1.81 | DFS | 1.33 | 1.23 |
| 14 | 5064 | 180713 | 273 | 80 | 1.73 | DFS | 1.36 | 1.21 |
| 16 | 15872 | 180944 | 945 | 131 | 1.73 | DFS | 1.42 | 1.22 |
| 18 | 30135 | 112972 | 1322 | 309 | 1.69 | DFS | 1.39 | 1.26 |
| 20 | 57944 | 59359 | 4281 | 809 | 1.65 | DFS | 1.43 | 1.30 |
| 22 | 105737 | 180716 | 12865 | 1338 | 1.62 | DFS | 1.46 | 1.30 |
| 24 | 149124 | 93690 | 32305 | 2959 | 1.56 | DFS | 1.47 | 1.31 |
| 26 | 173054 | 162039 | 49519 | 5104 | 1.53 | DFS | 1.45 | 1.31 |

