# Cash Register Algorithms

## Overview
This project provides two functions to determine the optimal way to return change to a customer in a cash register system using different algorithms:

1. **Greedy Algorithm** (`find_coins_greedy`) - Uses a greedy approach to select coins from the highest to the lowest denomination.
2. **Dynamic Programming Algorithm** (`find_min_coins`) - Uses dynamic programming to find the optimal combination of coins that results in the minimum number of coins used.

## Algorithms

### Greedy Algorithm (`find_coins_greedy`)
The greedy algorithm aims to use the largest possible coin denominations first to provide the change. It continues this approach until the entire amount is covered. This is straightforward and efficient in many cases, but it does not guarantee the minimal number of coins.

**Complexity**: The time complexity is **O(n)**, where **n** is the number of available coin denominations. This algorithm is efficient but not always optimal for all coin systems.

**Example Output**: For the amount **113**, the greedy algorithm returns `{50: 2, 10: 1, 2: 1, 1: 1}`.

### Dynamic Programming Algorithm (`find_min_coins`)
The dynamic programming approach guarantees the optimal solution by evaluating all possible combinations to find the one with the fewest coins. It fills a table that represents the minimum number of coins required for each sub-amount until the final amount is reached.

**Complexity**: The time complexity is **O(n * m)**, where **n** is the number of coin denominations and **m** is the amount to be returned. This algorithm takes more time but ensures the optimal number of coins.

**Example Output**: For the amount **113**, the dynamic programming algorithm returns `{50: 2, 10: 1, 2: 1, 1: 1}`.

## Comparison

- **Efficiency**: The greedy algorithm is faster and simpler but may not always provide the optimal solution. It works well with common coin systems (like the one used in this project), but it could fail in more complex coin sets.
- **Optimality**: The dynamic programming algorithm is more computationally intensive, especially for large sums, but it guarantees the minimal number of coins.

### Practical Use Cases
- The **greedy algorithm** is suitable for real-time systems where performance is critical, and a near-optimal solution is acceptable.
- The **dynamic programming algorithm** is ideal when ensuring the minimal number of coins is essential, such as in systems that handle a wide variety of currencies or need to minimize the physical number of coins for logistical reasons.

## Conclusion
In this project, we implemented both greedy and dynamic programming solutions to solve the coin change problem. While the greedy algorithm is generally faster, the dynamic programming solution guarantees an optimal solution. Depending on the coin denominations used and the constraints of the problem, one algorithm may be more suitable than the other.

In general, for common coin systems like the one used in this project, the greedy algorithm often produces the correct and efficient result. However, the dynamic programming approach provides a more comprehensive solution that works regardless of the coin system's complexity.

