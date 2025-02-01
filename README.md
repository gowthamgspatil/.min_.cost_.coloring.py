# .min_.cost_.coloring.py


The given function `min_cost_coloring(dp)` is designed to solve a variation of the **"Minimum Cost Coloring of a Grid"** problem.

---

## **Understanding the Problem**
We are given a **cost matrix** `dp` of size `n × m`, where:

- `dp[i][j]` represents the cost of coloring the `i-th` row with color `j`.
- The constraint is that **adjacent rows cannot have the same color**.
- The goal is to determine the minimum total cost of coloring all rows while satisfying this constraint.

---

## **Approach and Explanation**
The function implements a **dynamic programming (DP) approach** with **space optimization** to efficiently compute the solution.

### **Key Idea**
Instead of maintaining a `2D` DP table, we keep track of only the two **smallest costs** from the previous row (`prev_min[0]` and `prev_min[1]`). This helps in quickly determining the minimum cost for the current row while avoiding conflicts with the previously chosen color.

---

### **Step-by-Step Explanation**
1. **Edge Cases**:
   - If `n == 0`, return `0` (no rows to color).
   - If `m < 2`, return `-1` (not enough colors to satisfy constraints).

2. **Initialize Tracking Variables**:
   - `prev_min` stores the two smallest values from the previous row. 
   - It is initialized as `[(0, -1), (0, -1)]`, where each pair consists of `(cost, color_index)`.

3. **Iterate Over Rows (`i` loop)**:
   - For each row `i`, maintain `curr_min` to store the two smallest coloring costs.

4. **Iterate Over Colors (`j` loop)**:
   - If the previous row's **minimum-cost color** (`prev_min[0]`) is **different** from the current color `j`, add `prev_min[0][0]` to `dp[i][j]`.
   - Otherwise, use the **second smallest cost** (`prev_min[1][0]`) to avoid conflicts.
   - Update `curr_min` to track the two smallest values for the current row.

5. **Update `prev_min`**:
   - After processing each row, update `prev_min` with `curr_min`, so the next row can use this information.

6. **Final Result**:
   - The answer is the **smallest value** in the last row, which gives the minimum total coloring cost.

---

## **Time and Space Complexity**
- **Time Complexity**: \( O(nm) \), since we iterate through all elements of the matrix once.
- **Space Complexity**: \( O(1) \), as we only maintain a few extra variables instead of storing a full DP table.

---

## **Example Walkthrough**
Consider a cost matrix:

\[
dp =
\begin{bmatrix}
1 & 5 & 3 \\
2 & 9 & 4 \\
6 & 2 & 8
\end{bmatrix}
\]

1. **First row (`i = 0`)**:  
   - `prev_min = [(1, 0), (3, 2)]` (smallest costs from the first row: 1 at index 0, and 3 at index 2).

2. **Second row (`i = 1`)**:  
   - For `j = 0`: It conflicts with `prev_min[0]`, so we use `prev_min[1] → dp[1][0] = 2 + 3 = 5`.
   - For `j = 1`: No conflict, so we use `prev_min[0] → dp[1][1] = 9 + 1 = 10`.
   - For `j = 2`: No conflict, so we use `prev_min[0] → dp[1][2] = 4 + 1 = 5`.  
   - `prev_min` is updated to `[(5, 0), (5, 2)]`.

3. **Third row (`i = 2`)**:  
   - For `j = 0`: It conflicts with `prev_min[0]`, so we use `prev_min[1] → dp[2][0] = 6 + 5 = 11`.
   - For `j = 1`: No conflict, so we use `prev_min[0] → dp[2][1] = 2 + 5 = 7`.
   - For `j = 2`: No conflict, so we use `prev_min[0] → dp[2][2] = 8 + 5 = 13`.  
   - `prev_min` is updated to `[(7, 1), (11, 0)]`.

4. **Result**:  
   - The minimum value in the last row is **7**, which is the minimum total coloring cost.

---

## **Conclusion**
This algorithm efficiently computes the minimum coloring cost while satisfying the adjacency constraint, making it an optimal **dynamic programming solution** with **space optimization**. 🚀
