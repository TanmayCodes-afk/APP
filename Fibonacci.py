# Fibonacci using Memoization and Tabulation

# Memoization
def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Tabulation
def fibonacci_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Input
n = int(input("Enter n: "))

# Output
print("Fibonacci using Memoization:", fibonacci_memo(n))
print("Fibonacci using Tabulation:", fibonacci_tab(n))