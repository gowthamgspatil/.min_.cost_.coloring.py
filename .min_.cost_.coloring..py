

import math

def min_cost_coloring(dp):
    n = len(dp)
    if n == 0:
        return 0
    m = len(dp[0])
    if m < 2:
        return -1

    prev_min = [(0, -1), (0, -1)]

    for i in range(n):
        curr_min = [(math.inf, -1), (math.inf, -1)]

        for j in range(m):
            if j != prev_min[0][1]:
                dp[i][j] += prev_min[0][0]
            else:
                dp[i][j] += prev_min[1][0]

            if curr_min[0][0] > dp[i][j]:
                curr_min[1] = curr_min[0]
                curr_min[0] = (dp[i][j], j)
            elif curr_min[1][0] > dp[i][j]:
                curr_min[1] = (dp[i][j], j)

        prev_min = curr_min

    return min(dp[n - 1])


