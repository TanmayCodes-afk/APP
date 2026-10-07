#Bottom-Up (Tabulation)
def knapsack_bottom_up(weights, values, W):
    n = len(weights)

    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Input
n, W = map(int, input().split())

weights = list(map(int, input().split()))
values = list(map(int, input().split()))

print(knapsack_bottom_up(weights, values, W))

#Top-Down (Memoization)
def knapsack_top_down(weights, values, n, W, memo):

    if n == 0 or W == 0:
        return 0

    if (n, W) in memo:
        return memo[(n, W)]

    if weights[n - 1] <= W:
        memo[(n, W)] = max(
            values[n - 1] + knapsack_top_down(
                weights, values, n - 1,
                W - weights[n - 1], memo
            ),
            knapsack_top_down(
                weights, values, n - 1, W, memo
            )
        )
    else:
        memo[(n, W)] = knapsack_top_down(
            weights, values, n - 1, W, memo
        )

    return memo[(n, W)]


# Input
n, W = map(int, input().split())

weights = list(map(int, input().split()))
values = list(map(int, input().split()))

memo = {}

print(knapsack_top_down(weights, values, n, W, memo))